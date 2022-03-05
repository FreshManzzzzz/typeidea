from rest_framework import serializers, pagination

from .models import Post, Category, Tag


# 写入文章数据的接口
class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content', 'created_time']


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tag = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    url = serializers.HyperlinkedIdentityField(view_name='api-post-detail')

    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'category', 'tag', 'owner', 'created_time']
        # extra_kwargs = {
        #     'url': {'view_name': 'api-post-detail'}
        # }


# 获取文章详情的serializer
class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content_html', 'created_time']


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-category-detail')

    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'created_time']


#  获取每个分类下的文章数据的serializer
class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'created_time', 'posts',
        )


class TagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-tag-detail')

    class Meta:
        model = Tag
        fields = ['id', 'url', 'name', 'created_time']


# 配置获取该tag下所有文章的serializer
class TagDeatilSerializer(TagSerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'created_time', 'posts',
        )
