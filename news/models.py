from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField # 安装：pip install DjangoUeditor


class News(models.Model):
    NewsType = (
        ('企业要闻', '企业要闻'),
        ('行业新闻', '行业新闻'),
        ('通知公告', '通知公告'),
    )

    title = models.CharField(max_length=50, verbose_name='新闻标题')
    news_description = UEditorField(u'内容', default='', width=950, height=280, imagePath='news/images',
                                    filePath='news/files')
    news_type = models.CharField(max_length=50, choices=NewsType, verbose_name='新闻类型')
    news_photo = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='展报')
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
    news_view = models.PositiveIntegerField(default=1, verbose_name='浏览量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '通知公告'
        ordering = ['-publish_date']
        db_table = 'dy_news'
