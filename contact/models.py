from django.db import models
from django.utils import timezone
from datetime import datetime


class JD(models.Model):
    """企业招聘信息"""

    title = models.CharField(max_length=50, verbose_name='招聘岗位')
    description = models.TextField(verbose_name='招聘要求')
    publish_date = models.DateTimeField(default=timezone.now, verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '招聘信息'
        ordering = ['-publish_date']
        db_table = 'dy_JD'


class Resume(models.Model):
    """简历信息"""

    # 性别
    GenderType = (
        ('男', '男'),
        ('女', '女'),
    )

    # 审批状态
    ApproveType = (
        (1, '待审批'),
        (2, '审批通过'),
        (3, '审批拒绝'),
    )

    name = models.CharField(max_length=50, verbose_name='姓名')
    ID_number = models.CharField(max_length=30, verbose_name='身份证号')
    gender = models.CharField(max_length=5, choices=GenderType, default='男', verbose_name='性别')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    birthday = models.DateField(default=datetime.strftime(datetime.now(), '%Y-%m-%d'), verbose_name='出生日期')
    education_background = models.CharField(max_length=50, default='本科', verbose_name='学历')
    graduate_institution = models.CharField(max_length=50, verbose_name='毕业院校')
    major = models.CharField(max_length=50, verbose_name='主修专业')
    apply_position = models.CharField(max_length=40, verbose_name='申请职位')
    experience = models.TextField(blank=True, null=True, verbose_name='项目经验')
    person_photo = models.ImageField(upload_to='contact/recruit/%Y-%m-%d', verbose_name='个人照片')
    approve_status = models.IntegerField(choices=ApproveType, default=1, verbose_name='审批状态')
    submit_date = models.DateTimeField(default=timezone.now, verbose_name='提交时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '简历信息'
        ordering = ('-submit_date', '-approve_status')
        db_table = 'dy_resume'


class Contact(models.Model):
    # 荣誉
    description = models.TextField(max_length=500, verbose_name='图片描述', blank=True, null=True)

    # 图片地址
    photo = models.ImageField(upload_to='award/', verbose_name='图片地址', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '联系我们'  # 在管理后台看到的表名
        db_table = 'dy_contact'  # 在数据库看到的表名
