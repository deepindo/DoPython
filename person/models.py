from django.db import models


class Person(models.Model):
    """
    人员管理
    主键、外键都要用到
    联合主键
    """

    # 性别
    GenderType = (
        ('男', '男'),
        ('女', '女'),
    )

    StateType = (
        (1, '有效'),
        (2, '失效'),
    )

    EducationBackgroundType = (
        ('高中', '高中'),
        ('大专', '大专'),
        ('本科', '本科'),
        ('研究生-硕士', '研究生-硕士'),
        ('研究生-博士', '研究生-博士'),
        ('其他', '其他'),
    )

    id = models.AutoField(verbose_name='序号', primary_key=True, )
    name = models.CharField(verbose_name='姓名', max_length=15, )
    icon = models.ImageField(verbose_name='头像', upload_to='icon/', )
    age = models.IntegerField(verbose_name='年龄', default=0, )
    person_code = models.CharField(verbose_name='编号', max_length=20, )
    gender = models.CharField(verbose_name='性别', choices=GenderType, default='男', max_length=5, )
    ID_number = models.CharField(verbose_name='身份证号', blank=False, null=False, max_length=18, )
    birthday = models.DateTimeField(verbose_name='出生年月')
    mobile_phone = models.CharField(verbose_name='手机号', max_length=11)
    contact_phone = models.CharField(verbose_name='联系电话', blank=True, null=True, max_length=30, )
    wechat = models.CharField(verbose_name='微信', blank=True, null=True, max_length=50, )
    QQ = models.CharField(verbose_name='QQ', blank=True, null=True, max_length=50, )
    email = models.EmailField(verbose_name='邮箱', blank=True, null=True, )
    weibo = models.CharField(verbose_name='微博', blank=True, null=True, max_length=50, )
    hobby = models.CharField(verbose_name='爱好', blank=True, null=True, max_length=50, )
    graduate_institution = models.CharField(verbose_name='毕业院校', max_length=100, )
    education_background = models.CharField(verbose_name='学历', choices=EducationBackgroundType, default='其他', max_length=30, )
    major = models.CharField(verbose_name='主修专业', max_length=100, )
    score = models.FloatField(verbose_name='成绩')
    residential_address = models.CharField(verbose_name='居住地址', blank=True, null=True, max_length=100, )
    native_place = models.CharField(verbose_name='籍贯', blank=True, null=True, max_length=100, )
    emergency_contact = models.CharField(verbose_name='紧急联系人', blank=True, null=True, max_length=20, )
    emergency_phone = models.BigIntegerField(verbose_name='紧急联系方式', blank=True, null=True, )
    state = models.IntegerField(verbose_name='状态', choices=StateType, default=1, )

    def __str__(self):
        return self.name

    # 重写save方法
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.person_code == '':

            new_count = Person.objects.count() + 1

            self.person_code = 'ID' + '%05d' % new_count

        super().save()

    class Meta:
        verbose_name = verbose_name_plural = '人员管理'
        db_table = 'dy_person'
