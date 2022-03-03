from django.contrib import admin
import xadmin

from blog.models import Post

from .models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = ('target', 'nickname', 'content', 'website', 'status', 'created_time')

    # 配置评论只显示当前用户所拥有文章的评论

    def get_queryset(self, request):
        current_user_posts = Post.objects.all().filter(owner=request.user)

        qs = super(CommentAdmin, self).get_queryset(request)
        return qs.filter(target__in=current_user_posts)
