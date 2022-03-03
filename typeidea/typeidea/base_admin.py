class BaseOwnerAdmin(object):
    """
    1.用于自动补充文章、分类、标签、侧边栏、友链这些Model的owner字段
    2.用于针对queryset过滤当前用户的数据
    """
    exclude = ['owner']

    # def get_queryset(self, request):
    #     qs = super(BaseOwnerAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)
    #
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()
