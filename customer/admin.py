from django.contrib import admin
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('customer_id', 'customer_name', 'institution', 'institution_code', 'gender', 'customer_type', 'customer_duty', 'customer_title', 'customer_phone', 'approve_status', 'create_date', )
    empty_value_display = ''
    fields = ('customer_name', 'institution', 'gender', 'customer_type', 'customer_duty', 'customer_title', 'customer_phone', 'approve_status', 'create_date', )
    list_display_links = ('customer_name', )
    ordering = ('customer_id', )
    list_per_page = 10
    list_filter = ('institution', 'customer_duty', 'customer_title',)
    search_fields = ('customer_name', 'institution',)
    actions = ('import_excel', 'export_excel_openpyxl', )

    # 若是在admin.py页面写，就得这样写，也可以直接在models.py中写，更加方便
    # def institution_code(self, obj):
    #     return obj.institution.institution_code

    """使用openpyxl导出excel"""
    def export_excel_openpyxl(self, request, queryset):
        pass
    export_excel_openpyxl.short_description = '导出Excel'

    def import_excel(self, request, queryset):
        pass
    import_excel.short_description = '导入Excel'


admin.site.register(Customer, CustomerAdmin)
