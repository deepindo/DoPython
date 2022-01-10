from django.db import models
from django.utils import timezone


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

    code = models.CharField(max_length=30, verbose_name='机构编码')
    name = models.CharField(max_length=30, verbose_name='机构名称')
    alias = models.CharField(max_length=30, blank=True, null=True, verbose_name='机构别名')
    province = models.CharField(max_length=20, verbose_name='省份')
    city = models.CharField(max_length=20, verbose_name='城市')
    area = models.CharField(max_length=20, blank=True, null=True, verbose_name='区县')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='详细地址')
    institution_type = models.CharField(max_length=100, choices=InstitutionType, default='其他', verbose_name='机构类别')
    institution_property = models.IntegerField(choices=InstitutionProperty, verbose_name='机构性质')
    institution_character = models.IntegerField(choices=InstitutionCharacter, verbose_name='机构属性')
    post_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='机构电话')
    approve_status = models.IntegerField(choices=ApproveType, default=1, verbose_name='审批状态')
    submit_date = models.DateTimeField(default=timezone.now, verbose_name='提交时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '机构信息'
        ordering = ('-submit_date', '-approve_status')
        db_table = 'dy_institution'
