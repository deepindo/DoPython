from django.db import models
from django.utils import timezone


class Document(models.Model):
    """资料下载"""

    title = models.CharField(max_length=40, verbose_name='资料名称')
    file = models.FileField(upload_to='Service/', blank=True, verbose_name='文件资料')
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='上传时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文件资料'
        ordering = ['-publish_date']
        db_table = 'dy_document'


