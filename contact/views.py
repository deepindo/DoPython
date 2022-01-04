from django.shortcuts import render
from contact.models import JD, Resume
from contact.forms import ResumeForm


def contact(request):
    """联系我们"""

    context = {
        'active_menu': 'employ',
        'sub_menu': 'contact',
    }

    return render(request, 'contact/contact.html', context)


def recruit(request):
    """人才招聘页面"""

    JDList = JD.objects.all().order_by('-publish_date')
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST, files=request.FILES)
        if resumeForm.is_valid():
            resumeForm.save()
            context = {
                'JDList': JDList,
                'sub_menu': 'recruit',
            }
            return render(request, 'contact/contact.html', context)
    else:
        resumeForm = ResumeForm()
        context = {
            'JDList': JDList,
            'sub_menu': 'recruit',
            'resumeForm': resumeForm,
        }
        return render(request, 'contact/recruit.html', context)