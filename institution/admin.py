from django.contrib import admin
from institution.models import Institution
import csv
from django.http import HttpResponse


class ExportCSV:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = '导出'


class InstitutionAdmin(admin.ModelAdmin):

    # 空值的展示
    empty_value_display = '/'

    # 要显示的字段
    # list_display = ('institution_code', 'name', 'alias', 'province', 'city', 'area', 'address', 'institution_type',
    #                 'institution_property', 'institution_character', 'post_number', 'phone', 'approve_status',
    #                 'create_date',)
    list_display = ('serial_number', 'institution_code', 'name', 'alias', 'full_address', 'institution_type',
                    'institution_property', 'institution_character', 'phone', 'post_number', 'approve_status',
                    'create_date', 'operate_detail',)

    # 可以点击跳转的字段, 可以设置为None，一个不要
    # list_display_links = None
    list_display_links = ('name',)

    # 对于添加和修改，只读字段的不同处理
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['institution_code', "institution_type", "institution_property", 'institution_character', 'approve_status',
                    'create_date', ]
        else:
            return ['institution_code', ]

    # 只读字段
    # readonly_fields = ('institution_code',)

    # 模糊搜索功能
    search_fields = ('code', 'name', 'alias', 'province', 'city', 'area', 'address',)

    # 筛选功能 admin.RelatedFieldListFilter, admin.EmptyFieldListFilter, admin.RelatedOnlyFieldListFilter
    list_filter = ('institution_type', 'institution_property', 'institution_character', 'create_date', 'approve_status',)

    # 不设置的时候，是降序，最近加的显示在最上面
    ordering = ('institution_code',)

    # 每页显示条目数
    list_per_page = 10

    # list_editable = ('phone',)
    # date_hierarchy = 'create_date'

    actions = ['approve_institution', ]
    # ["export_as_csv", ]

    # 以下两个要结合使用， 不生效？
    actions_on_bottom = True
    actions_on_top = False
    # action_form = ["A", "B",] # 这个干嘛的，不能用

    # actions_selection_counter =

    # 增加Institution页面-展示(展示在同一行的放在一个元祖中, 对于一个元祖中超过两个，那么这多个会相对上下距离较近)
    # fields = (
    # ('name', 'alias'), ('institution_code', 'institution_type'), ('institution_property', 'institution_character'),
    # ('province', 'city'), ('area', 'address'), ('post_number', 'phone'), 'approve_status', 'create_date',)

    fieldsets = (
        ('基本信息', {
            'fields': ('institution_code', ('name', 'alias'), ('province', 'city'), ('area', 'address'), ('phone', 'post_number'), )
        }),
        ('其他信息', {
            'fields': ('institution_type', 'institution_property', 'institution_character', 'approve_status', 'create_date',)
        }),
    )

    """自定义操作：批量审批"""
    def approve_institution(self, request, queryset):
        queryset.update(approve_status=2)
    approve_institution.short_description = "批量审批"

    # def export_excel(self, request, queryset):
    #     print("test export")
    #     # queryset.update()


admin.site.register(Institution, InstitutionAdmin)
