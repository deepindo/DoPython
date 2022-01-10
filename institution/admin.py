from django.contrib import admin
from institution.models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('code', 'name', 'alias', 'province', 'city', 'area', 'address', 'institution_type',
                    'institution_property', 'institution_character', 'post_number', 'phone', 'approve_status',
                    'submit_date',)

    # 增加Institution页面-展示(展示在同一行的放在一个元祖中, 对于一个元祖中超过两个，那么这多个会相对上下距离较近)
    fields = (('name', 'alias'), ('code', 'institution_type'), ('institution_property', 'institution_character'),
              ('province', 'city'), ('area', 'address'), ('post_number', 'phone'), 'approve_status', 'submit_date',)

    # 搜索功能
    search_fields = ('code', 'name')

    # 筛选功能 admin.RelatedFieldListFilter, admin.EmptyFieldListFilter, admin.RelatedOnlyFieldListFilter
    list_filter = ('institution_type', 'approve_status', 'institution_property',)

    # 不设置的时候，是降序，最近加的显示在最上面
    ordering = ['submit_date']


admin.site.register(Institution, InstitutionAdmin)