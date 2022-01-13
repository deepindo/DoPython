from django.contrib import admin
from institution.models import Institution
import csv
from django.http import HttpResponse, JsonResponse
from simpleui.admin import AjaxAdmin


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

    # 列表顶部全局按钮
    actions = ('button_batch_approve', 'button_export_excel', 'alert_batch_approve', 'upload_file', )
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
            'fields': ('institution_code', ('name', 'alias'), ('province', 'city'), ('area', 'address'), ('phone', 'post_number',), )
        }),
        ('其他信息', {
            'fields': ('institution_type', 'institution_property', 'institution_character', 'approve_status', 'create_date',)
        }),
    )

    """自定义操作：批量审批"""
    def button_batch_approve(self, request, queryset):
        print('-' * 10)
        print(request)
        print(queryset)
        queryset.update(approve_status=2)
    button_batch_approve.short_description = "批量审批"
    button_batch_approve.type = 'warning'
    button_batch_approve.style = 'color:black;'
    button_batch_approve.confirm = '您确定要批量审批选中的机构？'
    button_batch_approve.action_type = 2  # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    button_batch_approve.action_url = 'https://www.baidu.com'

    """自定义操作：导出"""
    def button_export_excel(self, request, queryset):
        print('button_export_excel click')
        pass
    button_export_excel.short_description = '导出'
    button_export_excel.icon = 'fas fa-audio-description' # 参考https://fontawesome.com
    button_export_excel.type = 'primary'  # 参考https://element.eleme.cn/#/zh-CN/component/button
    button_export_excel.style = 'color:black;'
    button_export_excel.confirm = '您确定要导出？'

    """上传文件"""
    def upload_file(self, request, queryset):
        upload = request.FILES['upload']
        print(upload)
        pass
    upload_file.short_description = '文件上传对话框'
    upload_file.type = 'success'
    upload_file.icon = 'el-icon-upload'
    upload_file.enable = True

    upload_file.layer = {
        'title': '文件上传',
        'params': [{
            'type': 'file',
            'key': 'upload',
            'label': '文件'
        }]
    }

    """自定义弹框：批量审批"""
    def alert_batch_approve(self, request, queryset):
        post = request.POST
        if not post.get('_selected'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据！'
            })
        else:
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功！'
            })

    alert_batch_approve.short_description = '批量审批弹框'
    alert_batch_approve.type = 'success'
    alert_batch_approve.icon = 'el-icon-s-promotion'

    alert_batch_approve.layer = {
        'title': '批量审批',
        'tips': '确定批量审批选中的机构？',
        'confirm_button': '审批通过',
        'cancel_button': '取消',

        'width': '40%',
        # 'height': '100px',
        'labelWidth': '80px',
        'params': [{
            'type': 'input',
            'key': 'remark',
            'label': '理由',
            'require': True,
            # 'size': 'medium',
            'width': '100%',
            'height': '200px',  # 不起效
        }, {
            'type': 'select',
            'key': 'type',
            'label': '类型',
            'width': '200px',
            # size对应elementui的size，取值为：medium / small / mini
            'size': 'small',
            # value字段可以指定默认值
            'value': '0',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }]
        }, {
            'type': 'number',
            'key': 'money',
            'label': '金额',
            # 设置默认值
            'value': 1000
        }, {
            'type': 'date',
            'key': 'date',
            'label': '日期',
        }, {
            'type': 'datetime',
            'key': 'datetime',
            'label': '时间',
        }, {
            'type': 'rate',
            'key': 'star',
            'label': '评价等级'
        }, {
            'type': 'color',
            'key': 'color',
            'label': '颜色'
        }, {
            'type': 'slider',
            'key': 'slider',
            'label': '滑块'
        }, {
            'type': 'switch',
            'key': 'switch',
            'label': 'switch开关'
        }, {
            'type': 'input_number',
            'key': 'input_number',
            'label': 'input number'
        }, {
            'type': 'checkbox',
            'key': 'checkbox',
            # 必须指定默认值
            'value': [],
            'label': '复选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }, {
            'type': 'radio',
            'key': 'radio',
            'label': '单选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }]
    }


admin.site.register(Institution, InstitutionAdmin)
