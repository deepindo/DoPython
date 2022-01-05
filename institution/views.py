from django.shortcuts import render
from institution.models import Institution
from django.http import JsonResponse


def institution_list(request):
    queryset = Institution.objects.all()
    arr = []
    for i in queryset:
        arr.append({
            'code': Institution.code,
            'name': Institution.name,
            'alias': Institution.alias,
            'province': Institution.province,
            'city': Institution.city,
            'area': Institution.area,
            'address': Institution.address,
            'institution_type': Institution.institution_type,
            'institution_property': Institution.institution_property,
            'institution_character': Institution.institution_character,
            'post_number': Institution.post_number,
            'phone': Institution.phone,
            'approve_status':  Institution.approve_status,
            'submit_date': Institution.submit_date,
        })
    return JsonResponse(arr, safe=False)

