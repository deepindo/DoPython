from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'ID_number', 'gender', 'email', 'birthday', 'education_background',
                  'graduate_institution', 'major', 'experience', 'apply_position', 'person_photo')

        education_background_type = (
            ('大专', '大专'),
            ('本科', '本科'),
            ('硕士', '硕士'),
            ('博士', '博士'),
            ('其他', '其他'),
        )

        widgets = {
            #'gender': forms.Select(choices=gender_type),
            'education_background': forms.Select(choices=education_background_type),
            'person_photo': forms.FileInput(),
        }