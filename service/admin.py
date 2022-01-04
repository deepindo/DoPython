from django.contrib import admin
from service.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file', 'publish_date')
    fields = ('title', 'file', 'publish_date')


admin.site.register(Document, DocumentAdmin)
