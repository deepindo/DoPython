from django.contrib import admin
from django.utils.safestring import mark_safe
from person.models import Person


# @admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_code', 'avatar', 'name', 'gender', 'age', 'ID_number', 'birthday', 'mobile_phone', 'graduate_institution', 'education_background', 'major', 'score', 'residential_address', 'native_place',
                    'emergency_contact', 'emergency_phone', 'state', 'operate',)  #  'contact_phone', 'wechat', 'QQ', 'email', 'weibo', 'hobby',
    list_display_links = ('name',)

    # 对于添加和修改，只读字段的不同处理
    def get_readonly_fields(self, request, obj=None):
        if obj:  # 编辑
            return ['person_code', 'ID_number', ]
        else:  # 新增
            return ['person_code', ]

    # 其他头像是用的icon，而列表中的自定义封装的avatar，不一样，要注意
    fieldsets = (
        ('基本信息', {
            'fields': ('person_code', 'name', 'icon', 'gender', 'age', 'ID_number', 'birthday', 'mobile_phone', 'graduate_institution', 'education_background', 'major', 'score', 'residential_address', 'native_place',
                       'emergency_contact', 'emergency_phone', 'state', )
        }),
        ('其他信息', {
            'fields': ('contact_phone', 'wechat', 'QQ', 'email', 'weibo', 'hobby',)
        }),
    )

    # 在list页面显示头像
    @admin.display(description='人员头像', ordering='name')
    def avatar(self, obj):
        div = f"<img src='{obj.icon.url}' width='32px'>"
        return mark_safe(div)

    # 定义一些操作示例
    @admin.display(description='操作', ordering='name')
    def operate(self, obj):
        info_msg = f"这个功能的名字是：{obj.name} 年龄是: {obj.age}"

        # simpleui 用的element ui ,可以使用el的类修改默认样式
        btn1 = f"""<button onclick="self.parent.app.$msgbox('{info_msg}')" class="el-button el-button--warning el-button--small">信息</button>"""

        # 在新标签中打开修改界面，url可以随意指定。自己可以多做尝试
        data = '{"name": "%s", "icon": "fas fa-user-tie", "url": "/admin/person/person/%d/change/"}' % (obj.name, obj.pk)

        btn2 = f"""<button onclick='self.parent.app.openTab({data})' class='el-button el-button--danger el-button--small'>修改</button>"""

        return mark_safe(f"<div>{btn1} {btn2}</div>")


admin.site.register(Person, PersonAdmin)