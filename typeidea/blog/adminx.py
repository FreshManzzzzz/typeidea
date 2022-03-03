import xadmin.sites
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from .models import Category, Tag, Post


# 演示在分类页面直接编辑文章的用法，内置（inline）StackedInline样式不同,可选择继承自admin.StackedInline，以获取不同的展示样式
class PostInline:
    form_layout = (
        Container(
            Row("title", "desc", "status", "tag", "content"),
        )
    )
    # 控制额外多几个
    extra = 1
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')

    fields = ('name', 'status', 'is_nav')

    # 将这两段代码抽象出来到一个基类BaseOwnerAdmin类中，继承该基类即可，该基类继承自admin.ModelAdmin
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(CategoryAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'post_count')

    fields = ('name', 'status')

    # 同上
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(TagAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'owner',
        'created_time', 'operator'
    ]
    list_display_links = []
    # 注意这里不是定义的filter类，而是字段名
    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    exclude = ('owner',)
    # 基础的fields
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    # fieldsets
    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',

            'content',
        )
    )

    # 配置多对多字段tag纵向展示以及默认的展示效果
    # filter_vertical = ('tag',)

    # 配置多对多字段tag横向展示以及默认的展示效果
    # filter_horizontal = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # 同上
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    # 配置自定义的网络css，该配置只适用于纵向展示，即wide，与filter_vertical同步使用
    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)

    # @property
    # def media(self):
    #     # # xadmin基于bootstrap，引入会页面样式冲突，仅供参考, 故注释。
    #     media = super().media()
    #     media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
    #     media.add_css({
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     })
    #     return media
