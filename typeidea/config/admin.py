from django.contrib import admin
from typeidea.custom_site import custom_site
from .models import Link, SideBar


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'owner', 'created_time')
    exclude = ('owner',)
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(LinkAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'owner', 'created_time')
    exclude = ('owner',)
    fields = ('title', 'display_type', 'content')
    list_filter = ['display_type', ]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(SideBarAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
