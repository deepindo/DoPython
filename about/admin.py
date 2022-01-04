from django.contrib import admin
from about.models import Award


class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'photo')
    fields = ('description', 'photo')


admin.site.register(Award, AwardAdmin)
admin.site.site_header = '苍玄天管理'
admin.site.site_title = '苍玄天_管理系统'
admin.site.index_title = '苍玄天_索引'
