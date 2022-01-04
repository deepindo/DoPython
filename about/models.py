from django.db import models


class Award(models.Model):
    # 荣誉
    description = models.TextField(max_length=500, verbose_name='图片描述', blank=True, null=True)

    # 图片地址
    photo = models.ImageField(upload_to='award/', verbose_name='图片地址', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = '荣誉资质'  # 在管理后台看到的表名
        db_table = 'dy_award'  # 在数据库看到的表名
