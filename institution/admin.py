from django.contrib import admin
from institution.models import Institution
import csv
from django.http import HttpResponse, JsonResponse
from simpleui.admin import AjaxAdmin
from django.utils import timezone

import xlwt as xlwt
from io import BytesIO


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
        if obj:  # 编辑
            return ['institution_code', "institution_type", "institution_property", 'institution_character', 'approve_status',
                    'create_date', ]
        else:  # 新增
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

    """自定义操作：导出Excel"""
    def button_export_excel(self, request, queryset):

        # 这个for循环是为了在多选的时候只导出第一个文件，避免多个被同时导出
        for i in queryset:
            filename = str(i)
            print(filename)
            break

        response = HttpResponse(content_type='application/vnd.ms-excel')
        # response['Content-Disposition'] = 'attachment;filename=20220117.xlsx'  # 这个表名为何不能用中文

        for i in Institution.objects.all().filter(name = filename):
            filename = i.serial_number
            filename = filename.encode('gb2312')  # 为了能将导出的excel命名为中文，必须转成gb2312
            typess = 'attachment;filename='+filename+'.xlsx'  # 这一步命名导出的excel，为登记的case名称
            response['Content-Disposition'] = typess

        # 创建excel文件对象
        excel_file = xlwt.Workbook(encoding='utf-8')

        # 创建一个sheet对象
        excel_sheet = excel_file.add_sheet('机构信息', cell_overwrite_ok=True)  # 创建的sheet名称为机构信息，注意如果想要开启覆盖写入，必须将overwrite功能开启

        # 定义字体和表格样式：
        # 接下里是定义表格的样式，如果你想对不同的表格定义不同的样式只能采用下面这种方式，否则将会默认成一种格式，即使定义了不同的变量，也会影响全局变量
        style_heading = xlwt.easyxf("""
          font: # 字体设置
            name Microsoft YaHei,  # 定义字体为微软雅黑
            colour_index black,  # 字体颜色为黑色
            bold off,  # 不加粗
            height 200; #字体大小 此处的200实际对应的字号是10号
          align: # 对齐方式设置
            wrap off, #自动换行 关闭
            vert center, #上下居中
            horiz center; #左右居中
          pattern: #表格样式设置
            pattern solid, 
            fore-colour white; # 表格颜色 白色
          borders: # 表格外框设置
            left THIN, #THIN 为实线
            right THIN,
            top THIN,
            bottom THIN; 
          """)

        style_playback = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index black,
            bold off,
            height 200;
          align:
            wrap 1, # 此处设置为1时表示开启自动换行
            vert center,
            horiz left;
          pattern:
            pattern solid,
            fore-colour white;
          borders:
            left THIN,
            right THIN,
            top THIN,
            bottom THIN;
          """)

        style_time_s = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index black,
            bold off,
            height 200;
          align:
            wrap off,
            vert center,
            horiz center;
          pattern:
            pattern solid,
            fore-colour white;
          borders:
            left THIN,
            right THIN,
            top THIN,
            bottom THIN;
          """, num_format_str='YYYY-MM-DD')  # 设置时间格式样式为 2019-03-01

        style_time = style_heading
        style_time.num_format_str = 'YYYY-MM-DD hh:mm'  # 设置时间格式样式为 2019-03-01 17:30

        # # 接下来是合并单元格，这个是一个比较细的工作：
        # # 合并单元格 顺序是从0开始
        # excel_sheet.write_merge(0, 0, 1, 3,) # 参数说明为 从第0行到第0行的第1列到第3列合并
        # excel_sheet.write_merge(2, 3, 1, 5,) # 参数说明为 从第2行到第3行的第1列到第5列合并
        # # 多行执行相同的合并可以写个for循环
        # for i in range(6,12):
        #     excel_sheet.write_merge(i,i,1,3,) # 相当于在6到12行的第1列到第3列分别合并 如果这个逻辑绕不明白可以自己实践一下
        # # 接下来是添加边框，因为合并了单元格不等于自动加边框，导致导出的表格里有未加边框的情况，所以只能先行添加好
        # # 添加边框，可以用两个for来实现，具体逻辑可自行根据实际情况修改
        # for i in range(6,12):
        #     for j in range(1,6):
        #         excel_sheet.write(i,j,'',style_heading)

        # 定义表格的宽度和高度
        row1 = excel_sheet.col(0)
        row1.width = 80*80
        row2 = excel_sheet.col(1)
        row2.width = 80*80
        row3 = excel_sheet.col(2)
        row3.width = 80*80
        row4 = excel_sheet.col(3)
        row4.width = 80*80
        row5 = excel_sheet.col(4)
        row5.width = 80*80
        row6 = excel_sheet.col(5)
        row6.width = 80*80
        row7 = excel_sheet.col(6)
        row7.width = 80*80
        row8 = excel_sheet.col(7)
        row8.width = 80*80
        row9 = excel_sheet.col(8)
        row9.width = 80*80
        row10 = excel_sheet.col(9)
        row10.width = 80*80
        row11 = excel_sheet.col(10)
        row11.width = 80*80
        row12 = excel_sheet.col(11)
        row12.width = 80*80
        row13 = excel_sheet.col(12)
        row13.width = 80*80
        row14 = excel_sheet.col(13)
        row14.width = 80*80
        row15 = excel_sheet.col(14)
        row15.width = 80*80

        # sheet.row(0).height_mismatch = True # 高度可不依赖字体大小定义，定义高度时最好开启此选项
        # sheet.row(0).height = 40*20
        # ...
        # for i in range(7,12): # 也可以通过for循环批量定义高度或宽度
        #     sheet.row(i).height_mismatch = True
        #     sheet.row(i).height = 40*20

        # 写入文件标题
        # excel_sheet.write(0, 0, '序号', xlwt.easyxf('font: height 240, colour_index red,')) # 一个一个写可以这样，也可以如下，适配样式
        excel_sheet.write(0, 0, '序号', style_heading)
        excel_sheet.write(0, 1, '机构编码', style_heading)
        excel_sheet.write(0, 2, '机构名称', style_heading)
        excel_sheet.write(0, 3, '机构别名', style_heading)
        excel_sheet.write(0, 4, '省份', style_heading)
        excel_sheet.write(0, 5, '城市', style_heading)
        excel_sheet.write(0, 6, '区县', style_heading)
        excel_sheet.write(0, 7, '详细地址', style_heading)
        excel_sheet.write(0, 8, '机构类别', style_heading)
        excel_sheet.write(0, 9, '机构性质', style_heading)
        excel_sheet.write(0, 10, '机构属性', style_heading)
        excel_sheet.write(0, 11, '邮政编码', style_heading)
        excel_sheet.write(0, 12, '机构电话', style_heading)
        excel_sheet.write(0, 13, '审批状态', style_heading)
        excel_sheet.write(0, 14, '创建时间', style_heading)

        # 写入数据
        for i in Institution.objects.all().filter(name=filename):  # 查询要写入的数据
            excel_sheet.write(0, 1, i.serial_number, style_playback)
            excel_sheet.write(1, 5, i.institution_code, style_heading)
            excel_sheet.write(2, 1, i.name, style_time)
            excel_sheet.write(3, 3, i.alias, style_time)
            excel_sheet.write(4, 3, i.province, style_time)
            excel_sheet.write(5, 3, i.city, style_time)
            excel_sheet.write(6, 3, i.area, style_time)
            excel_sheet.write(7, 3, i.address, style_time)
            excel_sheet.write(8, 3, i.institution_type, style_time)
            excel_sheet.write(9, 3, i.institution_property, style_time)
            excel_sheet.write(10, 3, i.institution_character, style_time)
            excel_sheet.write(11, 3, i.post_number, style_time)
            excel_sheet.write(12, 3, i.phone, style_time)
            excel_sheet.write(13, 3, i.approve_status, style_time)
            excel_sheet.write(14, 3, i.create_date, style_time)

        # 写出到IO
        output = BytesIO()
        excel_file.save(output)

        # 重新定位到开始
        output.seek(0)
        response.write(output.getvalue())
        return response


        # response = HttpResponse(content_type='application/vnd.ms-excel')
        # response['Content-Disposition'] = 'attachment;filename=20220117.xlsx'  # 这个表名为何不能用中文
        # workbook.save(response)
        # return response

    button_export_excel.short_description = '导出Excel'
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
