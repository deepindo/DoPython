from django.contrib import admin
from institution.models import Institution


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'alias', 'province', 'city', 'area', 'address', 'institution_type',
                    'institution_property', 'institution_character', 'post_number', 'phone', 'approve_status', 'submit_date', )
    fields = ('code', 'name', 'alias', 'province', 'city', 'area', 'address', 'institution_type','institution_property',
              'institution_character', 'post_number', 'phone', 'approve_status', 'submit_date', )


admin.site.register(Institution, InstitutionAdmin)