from django.shortcuts import render
from blog.models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    #
    # if tag_id:
    #     try:
    #         tag = Tag.objects.get(id=tag_id)
    #     except Tag.DoseNotExist:
    #         post_list = []
    #     else:
    #         post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    # else:
    #     post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
    #     if category_id:
    #         try:
    #             category = Category.objects.get(id=category_id)
    #         except Category.DoesNotExist:
    #             category = None
    #         else:
    #             post_list = post_list.filter(category_id=category_id)
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:

        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'tag': tag,
        'category': category,
        'post_list': post_list,

    }
    context.update(Category.get_navs())

    context.update(get_sidebardata())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post': post,
    }
    context.update(Category.get_navs())
    context.update(get_sidebardata())

    return render(request, 'blog/detail.html', context=context)


def get_sidebardata():
    sidebars = SideBar.get_all()
    recently_posts = Post.latest_posts()
    hot_posts = Post.hot_posts()
    comments = Comment.objects.filter(status=Comment.STATUS_NORMAL)
    context = {
        'sidebars': sidebars,
        'recently_posts': recently_posts,
        'hot_posts': hot_posts,
        'comments': comments,
    }

    return context
