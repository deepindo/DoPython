from django.contrib import admin
from contact.models import JD, Resume, Contact
from django.utils.safestring import mark_safe


class JDAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'publish_date')
    fields = ('title', 'description', 'publish_date')


admin.site.register(JD, JDAdmin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ID_number', 'gender', 'email', 'birthday', 'education_background', 'graduate_institution',
                    'major', 'apply_position', 'experience', 'image_data', 'submit_date', 'approve_status', )

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="120px"/>' % obj.person_photo.url)

    image_data.short_description = u'个人照片'


admin.site.register(Resume, ResumeAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'photo')
    fields = ('description', 'photo')


admin.site.register(Contact, ContactAdmin)
