from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_type', 'title', 'publish_date', 'news_view')
    style_fields = {'news_description': 'ueditor'}


admin.site.register(News, NewsAdmin)
