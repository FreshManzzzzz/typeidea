"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from blog.views import (
    IndexView, CategoryView, TagView, PostDetailView,
    SearchView, AuthorView,
    Handler404, Handler50x
)
from comment.views import CommentView
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from blog.apis import PostViewSet, CategoryViewSet, TagViewSet, PostWriteViewSet
from .custom_site import custom_site
import xadmin
from .autocomplete import CategoryAutocomplete, TagAutocomplete
from django.views.decorators.cache import cache_page
from config.views import LinkListView
from django.views.static import serve
import re

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')
router.register(r'tag', TagViewSet, base_name='api-tag')
router.register(r'post_write', PostWriteViewSet, base_name='api-post_write')

# 处理404，500错误页面的视图
handler404 = Handler404.as_view()
handler500 = Handler50x.as_view()


def static(prefix, **kwargs):
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve, kwargs=kwargs),
    ]


urlpatterns = [
                  url(r'^$', cache_page(60 * 1)(IndexView.as_view()), name='index'),
                  url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
                  url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
                  url(r'^post/(?P<post_id>\d+).html', PostDetailView.as_view(), name='post-detail'),
                  url(r'^links/$', LinkListView.as_view(), name='links'),
                  url(r'^search/$', SearchView.as_view(), name='search'),
                  url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author-list'),
                  url(r'^comment/$', CommentView.as_view(), name='comment'),
                  url(r'^super_admin/', admin.site.urls, name='super-admin'),
                  url(r'^admin/', xadmin.site.urls, name='xadmin'),
                  url(r'^rss|feed', LatestPostFeed(), name='rss'),
                  url(r'sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
                  url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name="category-autocomplete"),
                  url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name="tag-autocomplete"),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'^api/', include(router.urls)),
                  url(r'^api/docs/', include_docs_urls(title='typeidea apis')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                      # url(r'silk/',include('silk.urls',namespace='silk'))
                  ] + urlpatterns
