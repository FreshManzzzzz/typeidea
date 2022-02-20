from django.contrib import admin
from typeidea.custom_site import custom_site
from .models import Link, SideBar
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'owner', 'created_time')
    exclude = ('owner',)
    fields = ('title', 'href', 'status', 'weight')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(LinkAdmin, self).save_model(request, obj, form, change)
    #
    # def get_queryset(self, request):
    #     qs = super(LinkAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'owner', 'created_time')
    exclude = ('owner',)
    fields = ('title', 'display_type', 'content')
    list_filter = ['display_type', ]


