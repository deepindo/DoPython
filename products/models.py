from django.db import models
from django.utils import timezone


class Product(models.Model):
    """产品的数据表"""

    ProductType = (
        ('家用机器人', '家用机器人'),
        ('智能门锁', '智能门锁'),
        ('人脸识别解决方案', '人脸识别解决方案')
    )

    title = models.CharField(max_length=100, verbose_name='产品名称')
    photo = models.ImageField(upload_to='Product/', blank=True, verbose_name="产品图片")
    description = models.TextField(verbose_name="产品描述")
    product_type = models.CharField(choices=ProductType, max_length=100, verbose_name='产品类型')
    price = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True,
                                verbose_name='产品价格')  # decimal_places小数点的最大位数
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name="发布时间")
    product_views = models.PositiveIntegerField(default=1, verbose_name="浏览量")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "产品列表"
        ordering = ['-publish_date']
        db_table = 'dy_product'
