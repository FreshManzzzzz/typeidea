from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category, Tag
from .serializers import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer, TagSerializer,
    CategoryDetailSerializer, TagDeatilSerializer,
    PostWriteSerializer,
)


class PostWriteViewSet(viewsets.ModelViewSet):
    serializer_class = PostWriteSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    # permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDeatilSerializer
        return super().retrieve(request, *args, **kwargs)
