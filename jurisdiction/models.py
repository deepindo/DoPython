from django.db import models
from django.utils import timezone


class Jurisdiction(models.Model):
    """辖区信息"""

    # 辖区级别
    # JurisdictionLevel = (
    #     ('专科医院', '专科医院'),
    #     ('综合医院', '综合医院'),
    #     ('单体药店', '单体药店'),
    #     ('连锁药店门店', '连锁药店门店'),
    #     ('连锁药店总店', '连锁药店总店'),
    #     ('诊所', '诊所'),
    #     ('其他', '其他'),
    # )

    # 审批状态
    ApproveType = (
        (1, '待审批'),
        (2, '审批通过'),
        (3, '审批拒绝'),
    )

    jurisdiction_code = models.CharField(max_length=30, verbose_name='辖区编码')
    jurisdiction_name = models.CharField(max_length=30, verbose_name='辖区名称')
    jurisdiction_level = models.CharField(max_length=20, blank=True, null=True, verbose_name='辖区级别')
    remark = models.TextField(max_length=200, blank=True, null=True, verbose_name='备注')
    approve_status = models.IntegerField(choices=ApproveType, default=1, verbose_name='审批状态')
    submit_date = models.DateTimeField(default=timezone.now, verbose_name='提交时间')

    def __str__(self):
        return self.jurisdiction_name

    class Meta:
        verbose_name = verbose_name_plural = '辖区信息'
        ordering = ('-submit_date', '-approve_status')
        db_table = 'dy_jurisdiction'