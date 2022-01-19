from django.db import models
from django.utils import timezone
from institution.models import Institution


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

    # 客户职称
    CustomerTitle = (
        ('主任医师', '主任医师'),
        ('副主任医师', '副主任医师'),
        ('主治医师', '主治医师'),
        ('住院医师', '住院医师'),
        ('医生', '医生'),
        ('实习医生', '实习医生'),
        ('其他', '其他'),
    )

    # 客户职务
    CustomerDuty = (
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

    # institution_code = models.CharField(max_length=30, verbose_name='机构编码')
    # institution_name = models.CharField(max_length=30, verbose_name='机构名称')
    customer_id = models.AutoField(verbose_name='序号', primary_key=True, unique=True, )
    customer_name = models.CharField(verbose_name='客户姓名', max_length=20, )
    gender = models.CharField(verbose_name='性别', max_length=5, choices=GenderType, default='男', )
    customer_type = models.CharField(verbose_name='客户类型', max_length=10, choices=CustomerType, default='医生', )
    customer_duty = models.CharField(verbose_name='客户职务', max_length=10, choices=CustomerDuty, default='其他', )
    customer_title = models.CharField(verbose_name='客户职称', max_length=10, choices=CustomerTitle, default='其他', )
    customer_phone = models.CharField(verbose_name='客户电话', max_length=20, blank=True, null=True, )
    approve_status = models.IntegerField(verbose_name='审批状态', choices=ApproveType, default=1, )
    create_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now, )
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, db_column='institution_id',
                                    verbose_name='机构名称', )  # 对于警告：PEP 8:E501 line too long, 只要换行就可以了

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = verbose_name_plural = '客户信息'
        # ordering = ('-submit_date', '-approve_status')  # 排序可以在admin.py中写
        # 联合主键：seq_no，order_id，mac作为联合主键保证数据不重复，这里字段是举例子，具体场景再看
        # unique_together = ('seq_no', 'order_id', 'mac',)
        db_table = 'tb_customer'

    # 外键中的机构编码
    def institution_code(self):
        return self.institution.institution_code
    institution_code.short_description = '机构编码'


