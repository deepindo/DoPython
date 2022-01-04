from django.shortcuts import render
from about.models import Award


def survey(request):
    return render(request, 'about/survey.html', {'active_menu': 'about', 'sub_menu': 'survey'})


def honor(request):
    awards = Award.objects.all()
    context = {
        'awards': awards,
        'active_menu': 'about',
        'sub_menu': 'honor',
    }
    return render(request, 'about/honor.html', context)
