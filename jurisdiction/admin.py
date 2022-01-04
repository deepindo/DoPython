from django.contrib import admin
from jurisdiction.models import Jurisdiction


class JurisdictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'jurisdiction_code', 'jurisdiction_name', 'jurisdiction_level', 'approve_status', 'submit_date', )
    fields = ('jurisdiction_code', 'jurisdiction_name', 'jurisdiction_level', 'approve_status', 'submit_date',)


admin.site.register(Jurisdiction, JurisdictionAdmin)