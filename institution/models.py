from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
import uuid


class Institution(models.Model):
    """机构信息"""

    # 机构类型
    InstitutionType = (
        ('专科医院', '专科医院'),
        ('综合医院', '综合医院'),
        ('单体药店', '单体药店'),
        ('连锁药店门店', '连锁药店门店'),
        ('连锁药店总店', '连锁药店总店'),
        ('诊所', '诊所'),
        ('其他', '其他'),
    )

    # 机构性质
    InstitutionProperty = (
        (1, '民营医院'),
        (2, '公立医院'),
        (3, '专科医院'),
        (4, '未知'),
    )

    # 机构属性
    InstitutionCharacter = (
        (1, 'Common'),
        (2, 'COE'),
        (3, 'Focus'),
    )

    # 审批状态
    ApproveType = (
        (1, '待审批'),
        (2, '审批通过'),
        (3, '审批拒绝'),
    )

    """模型字段"""
    institution_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    serial_number = models.IntegerField(verbose_name='序号', default=1, blank=False, null=False, )
    institution_code = models.CharField(verbose_name='机构编码', max_length=20, )
    name = models.CharField(verbose_name='机构名称', max_length=50, )
    alias = models.CharField(verbose_name='机构别名', max_length=50, blank=True, null=True, )
    province = models.CharField(verbose_name='省份', max_length=20, )
    city = models.CharField(verbose_name='城市', max_length=20, )
    area = models.CharField(verbose_name='区县', max_length=20, blank=True, null=True, )
    address = models.CharField(verbose_name='详细地址', max_length=100, blank=True, null=True, )
    institution_type = models.CharField(verbose_name='机构类别', max_length=100, choices=InstitutionType, )
    institution_property = models.IntegerField(verbose_name='机构性质', choices=InstitutionProperty, )
    institution_character = models.IntegerField(verbose_name='机构属性', choices=InstitutionCharacter, default=1, )
    post_number = models.CharField(verbose_name='邮政编码', max_length=20, blank=True, null=True, )
    phone = models.CharField(verbose_name='机构电话', max_length=20, blank=True, null=True, )
    approve_status = models.IntegerField(verbose_name='审批状态', choices=ApproveType, default=1, )
    create_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '机构信息'
        # ordering = ('-submit_date', '-approve_status')
        db_table = 'dy_institution'

    # 重写save方法
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # 若是self.institution_code为None，才是insert数据，而不是update数据
        # if self.institution_code is None: # 不知道为何这个判断逻辑不生效了
        if self.institution_code is None or self.institution_code == '':
            print('institution_code为空')
            print(self.institution_code)

            # 获取数据库当前数据条数, 新的将在当前基础上加1
            new_count = Institution.objects.count() + 1

            # 对于机构编码institution_code，也可以用另外一种方法实现：self.institution_code = 'HA' + new_count.zfill(6)
            self.institution_code = 'HA' + '%06d' % new_count

            # 序号
            self.serial_number = new_count

        super().save()

    # 自定义显示字段：完整地址
    def full_address(self):
        return self.province + '-' + self.city + '' + self.area + '' + self.address
    full_address.short_description = '机构地址'

    # 自定义添加操作动作
    def operate_detail(self):
        return mark_safe('<a href="www.baidu.com" target="blank">详情</a>')
    operate_detail.short_description = "操作"
