from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=15, verbose_name='人员姓名')
    icon = models.ImageField(upload_to='icon/', verbose_name='人员头像')
    age = models.IntegerField(default=0, verbose_name='人员年龄')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '人员管理'
        db_table = 'dy_person'
