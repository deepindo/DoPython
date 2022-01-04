from django.db import models
from django.utils import timezone


class Customer(models.Model):
    """客户信息"""

    # 性别
    GenderType = (
        ('男', '男'),
        ('女', '女'),
    )

    # 客户类型
    CustomerType = (
        ('医生', '医生'),
        ('药剂师', '药剂师'),
        ('KDM', 'KDM'),
    )

    # 客户职务
    CustomerDuty = (
        ('主任医师', '主任医师'),
        ('副主任医师', '副主任医师'),
        ('主治医师', '主治医师'),
        ('住院医师', '住院医师'),
        ('医生', '医生'),
        ('实习医生', '实习医生'),
        ('其他', '其他'),
    )

    # 客户职称
    CustomerTitle = (
        ('院长', '院长'),
        ('副院长', '副院长'),
        ('主任', '主任'),
        ('副主任', '副主任'),
        ('组长', '组长'),
        ('副组长', '副组长'),
        ('其他', '其他'),
    )

    # 审批状态
    ApproveType = (
        (1, '待审批'),
        (2, '审批通过'),
        (3, '审批拒绝'),
    )

    institution_code = models.CharField(max_length=30, verbose_name='机构编码')
    institution_name = models.CharField(max_length=30, verbose_name='机构名称')
    customer_name = models.CharField(max_length=20, verbose_name='客户姓名')
    gender = models.CharField(max_length=5, choices=GenderType, default='男', verbose_name='性别')
    customer_type = models.CharField(max_length=10, choices=CustomerType, default='医生', verbose_name='客户类型')
    customer_duty = models.CharField(max_length=10, choices=CustomerDuty, default='其他', verbose_name='客户职务')
    customer_title = models.CharField(max_length=10, choices=CustomerTitle, default='其他', verbose_name='客户职称')
    customer_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='客户电话')
    approve_status = models.IntegerField(choices=ApproveType, default=1, verbose_name='审批状态')
    submit_date = models.DateTimeField(default=timezone.now, verbose_name='提交时间')

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = verbose_name_plural = '客户信息'
        ordering = ('-submit_date', '-approve_status')
        db_table = 'dy_customer'
