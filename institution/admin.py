from django.contrib import admin
from institution.models import Institution
from django.http import HttpResponse, JsonResponse
import xlwt as xlwt  # 导出Excel框架
from io import BytesIO
import datetime

# 下面的暂时不用，或者没有用
import csv
from simpleui.admin import AjaxAdmin
from django.utils import timezone
import time


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
            return ['institution_code', "institution_type", "institution_property", 'institution_character',
                    'approve_status',
                    'create_date', ]
        else:  # 新增
            return ['institution_code', ]

    # 只读字段
    # readonly_fields = ('institution_code',)

    # 模糊搜索功能
    search_fields = ('code', 'name', 'alias', 'province', 'city', 'area', 'address',)

    # 筛选功能 admin.RelatedFieldListFilter, admin.EmptyFieldListFilter, admin.RelatedOnlyFieldListFilter
    list_filter = (
        'institution_type', 'institution_property', 'institution_character', 'create_date', 'approve_status',)

    # 不设置的时候，是降序，最近加的显示在最上面
    ordering = ('institution_code',)

    # 每页显示条目数
    list_per_page = 10

    # list_editable = ('phone',)
    # date_hierarchy = 'create_date'

    # 列表顶部全局按钮
    actions = ('button_batch_approve', 'button_export_excel', 'alert_batch_approve', 'upload_file',)
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
            'fields': ('institution_code', ('name', 'alias'), ('province', 'city'), ('area', 'address'),
                       ('phone', 'post_number',),)
        }),
        ('其他信息', {
            'fields': (
                'institution_type', 'institution_property', 'institution_character', 'approve_status', 'create_date',)
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

    """使用openpyxl导出excel"""
    def export_excel_openpyxl(self, request, queryset):
        pass

    """自定义操作：导出Excel"""
    def button_export_excel(self, request, queryset):

        """关于python中的时间"""
        # print(time)  # <module 'time' (built-in)>
        # print(datetime.datetime.now())  # <module 'time' (built-in)>
        # print(timezone.now())  #  2022-01-18 07:21:15.674924+00:00

        file_name = '机构信息' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        # 这一步很重要，不这样做，导出的文件将是：下载.xlw，当然英文名不受影响，可以正常导出
        file_name = file_name.encode('utf-8').decode('ISO-8859-1')
        attachment_name = 'attachment;filename=' + file_name + '.xlsx'
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = attachment_name
        # response['Content-Disposition'] = 'attachment;filename={0}'.format(urlquote) + '.xlsx'

        # 创建excel文件对象
        excel_file = xlwt.Workbook(encoding='utf-8')

        # 创建一个sheet对象
        # 创建的sheet名称为机构信息，注意如果想要开启覆盖写入，必须将overwrite功能开启
        excel_sheet = excel_file.add_sheet('机构信息', cell_overwrite_ok=True)

        # 定义字体和表格样式：
        # 接下里是定义表格的样式，如果你想对不同的表格定义不同的样式只能采用下面这种方式，
        # 否则将会默认成一种格式，即使定义了不同的变量，也会影响全局变量
        # style_heading = xlwt.easyxf("""
        # font: # 字体设置
        # name Microsoft YaHei,  # 定义字体为微软雅黑
        # colour_index black,  # 字体颜色为黑色
        # bold off,  # 不加粗
        # height 200; #字体大小 此处的200实际对应的字号是10号
        # align: # 对齐方式设置
        # wrap off, #自动换行 关闭
        # vert center, #上下居中
        # horiz center; #左右居中
        # pattern: #表格样式设置
        # pattern solid,
        # fore-colour white; # 表格颜色 白色
        # borders: # 表格外框设置
        # left THIN, #THIN 为实线
        # right THIN,
        # top THIN,
        # bottom THIN;
        # """)

        # 表头的红色style
        head_style_red = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index red,
            bold on,
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
          """)

        # 表头的黑色style
        head_style_black = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index black,
            bold on,
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
          """)

        """wrap 1, # 此处设置为1时表示开启自动换行"""
        # 表内容
        body_style = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index black,
            bold off,
            height 200;
          align:
            wrap 1,
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

        # 表内容居中
        body_style_center = xlwt.easyxf("""
          font:
            name Microsoft YaHei,
            colour_index black,
            bold off,
            height 200;
          align:
            wrap 1,
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
          """)

        # 表内容_日期
        body_style_time = xlwt.easyxf("""
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
        # body_style_time = body_style_center
        # body_style_time.num_format_str = 'YYYY-MM-DD hh:mm'  # 设置时间格式样式为 2019-03-01 17:30
        # fmts = [
        #     'M/D/YY',
        #     'D-MMM-YY',
        #     'D-MMM',
        #     'MMM-YY',
        #     'h:mm AM/PM',
        #     'h:mm:ss AM/PM',
        #     'h:mm',
        #     'h:mm:ss',
        #     'M/D/YY h:mm',
        #     'mm:ss',
        #     '[h]:mm:ss',
        #     'mm:ss.0',
        # ]
        # body_style_time.num_format_str = fmts[0]

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
        row1.width = 1400
        row2 = excel_sheet.col(1)
        row2.width = 3000
        row3 = excel_sheet.col(2)
        row3.width = 6000
        row4 = excel_sheet.col(3)
        row4.width = 3000
        row5 = excel_sheet.col(4)
        row5.width = 1600
        row6 = excel_sheet.col(5)
        row6.width = 1600
        row7 = excel_sheet.col(6)
        row7.width = 1600
        row8 = excel_sheet.col(7)
        row8.width = 6400
        # row8.height_mismatch = True  # 高度可不依赖字体大小定义，定义高度时最好开启此选项
        row9 = excel_sheet.col(8)
        row9.width = 2300
        row10 = excel_sheet.col(9)
        row10.width = 2300
        row11 = excel_sheet.col(10)
        row11.width = 2300
        row12 = excel_sheet.col(11)
        row12.width = 2300
        row13 = excel_sheet.col(12)
        row13.width = 4300
        row14 = excel_sheet.col(13)
        row14.width = 2300
        row15 = excel_sheet.col(14)
        row15.width = 80 * 80

        # 写入文件标题
        # excel_sheet.write(0, 0, '序号', xlwt.easyxf('font: height 240, colour_index red,')) # 一个一个写可以这样，也可以如下，适配样式
        excel_sheet.write(0, 0, '序号', head_style_black)  # write方法后面，第一个数字是行数，第二个是列数
        excel_sheet.write(0, 1, '机构编码', head_style_black)
        excel_sheet.write(0, 2, '机构名称', head_style_red)
        excel_sheet.write(0, 3, '机构别名', head_style_black)
        excel_sheet.write(0, 4, '省份', head_style_red)
        excel_sheet.write(0, 5, '城市', head_style_red)
        excel_sheet.write(0, 6, '区县', head_style_black)
        excel_sheet.write(0, 7, '详细地址', head_style_black)
        excel_sheet.write(0, 8, '机构类别', head_style_red)
        excel_sheet.write(0, 9, '机构性质', head_style_red)
        excel_sheet.write(0, 10, '机构属性', head_style_red)
        excel_sheet.write(0, 11, '邮政编码', head_style_black)
        excel_sheet.write(0, 12, '机构电话', head_style_black)
        excel_sheet.write(0, 13, '审批状态', head_style_black)
        excel_sheet.write(0, 14, '创建时间', head_style_black)

        # 写入数据
        # 因为这里写入数据是根据一行一行添加的，所以要有一个索引，比如用row = 1, 每次循环完row = row + 1
        row = 1
        for i in Institution.objects.all().order_by('serial_number'):
            excel_sheet.write(row, 0, i.serial_number, body_style_center)
            excel_sheet.write(row, 1, i.institution_code, body_style_center)
            excel_sheet.write(row, 2, i.name, body_style)
            excel_sheet.write(row, 3, i.alias, body_style)
            excel_sheet.write(row, 4, i.province, body_style_center)
            excel_sheet.write(row, 5, i.city, body_style_center)
            excel_sheet.write(row, 6, i.area, body_style_center)
            excel_sheet.write(row, 7, i.address, body_style)
            excel_sheet.write(row, 8, i.institution_type, body_style_center)

            # 判断：机构性质
            if i.institution_property == 1:
                institution_property_value = '民营医院'
            elif i.institution_property == 2:
                institution_property_value = '公立医院'
            elif i.institution_property == 3:
                institution_property_value = '专科医院'
            elif i.institution_property == 4:
                institution_property_value = '未知'
            else:
                institution_property_value = '/'
            excel_sheet.write(row, 9, institution_property_value, body_style_center)

            # 判断：机构属性
            if i.institution_character == 1:
                institution_character_value = 'Common'
            elif i.institution_character == 2:
                institution_character_value = 'COE'
            elif i.institution_character == 3:
                institution_character_value = 'Focus'
            else:
                institution_character_value = '/'
            excel_sheet.write(row, 10, institution_character_value, body_style_center)
            excel_sheet.write(row, 11, i.post_number, body_style)
            excel_sheet.write(row, 12, i.phone, body_style)

            # 判断：审批状态
            if i.approve_status == 1:
                approve_status_value = '待审批'
            elif i.approve_status == 2:
                approve_status_value = '审批通过'
            elif i.approve_status == 3:
                approve_status_value = '审批拒绝'
            else:
                approve_status_value = '/'
            excel_sheet.write(row, 13, approve_status_value, body_style_center)

            # 时区对不上，要转一下格式
            create_date_value = i.create_date.strftime('%Y年%m月%d日 %H:%M:%S')
            excel_sheet.write(row, 14, create_date_value, body_style_time)
            row = row + 1

        # 或者用下面的enumerate的方法，就得列出索引:i, 以及值:v
        # for i, v in enumerate(Institution.objects.all().order_by('serial_number')):  # 查询要写入的数据
        #     excel_sheet.write(i + 1, 0, v.serial_number, body_style_center)
        #     excel_sheet.write(i + 1, 1, v.institution_code, body_style_center)
        #     excel_sheet.write(i + 1, 2, v.name, body_style)
        #     excel_sheet.write(i + 1, 3, v.alias, body_style)
        #     excel_sheet.write(i + 1, 4, v.province, body_style_center)
        #     excel_sheet.write(i + 1, 5, v.city, body_style_center)
        #     excel_sheet.write(i + 1, 6, v.area, body_style_center)
        #     excel_sheet.write(i + 1, 7, v.address, body_style)
        #     excel_sheet.write(i + 1, 8, v.institution_type, body_style_center)
        #
        #     # 判断：机构性质
        #     if v.institution_property == 1:
        #         institution_property_value = '民营医院'
        #     elif v.institution_property == 2:
        #         institution_property_value = '公立医院'
        #     elif v.institution_property == 3:
        #         institution_property_value = '专科医院'
        #     elif v.institution_property == 4:
        #         institution_property_value = '未知'
        #     else:
        #         institution_property_value = '/'
        #     excel_sheet.write(i + 1, 9, institution_property_value, body_style_center)
        #
        #     # 判断：机构属性
        #     if v.institution_character == 1:
        #         institution_character_value = 'Common'
        #     elif v.institution_character == 2:
        #         institution_character_value = 'COE'
        #     elif v.institution_character == 3:
        #         institution_character_value = 'Focus'
        #     else:
        #         institution_character_value = '/'
        #     excel_sheet.write(i + 1, 10, institution_character_value, body_style_center)
        #     excel_sheet.write(i + 1, 11, v.post_number, body_style)
        #     excel_sheet.write(i + 1, 12, v.phone, body_style)
        #
        #     # 判断：审批状态
        #     if v.approve_status == 1:
        #         approve_status_value = '待审批'
        #     elif v.approve_status == 2:
        #         approve_status_value = '审批通过'
        #     elif v.approve_status == 3:
        #         approve_status_value = '审批拒绝'
        #     else:
        #         approve_status_value = '/'
        #     excel_sheet.write(i + 1, 13, approve_status_value, body_style_center)
        #
        #     # 时区对不上，要转一下格式
        #     create_date_value = v.create_date.strftime('%Y年%m月%d日 %H:%M:%S')
        #     excel_sheet.write(i+1, 14, create_date_value, body_style_time)

        # 写出到IO
        output = BytesIO()  # 也有人这么写output = StringIO.StringIO()
        excel_file.save(output)

        # 重新定位到开始
        output.seek(0)
        response.write(output.getvalue())
        return response

    button_export_excel.short_description = '导出Excel'
    button_export_excel.icon = 'fas fa-audio-description'  # 参考https://fontawesome.com
    button_export_excel.type = 'primary'  # 参考https://element.eleme.cn/#/zh-CN/component/button
    button_export_excel.style = 'color:white;'
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
