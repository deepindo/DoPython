from django.shortcuts import render
from institution.models import Institution
from django.http import JsonResponse
from fastapi import FastAPI
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
# import requests

# app = FastAPI()


# @require_http_methods(['GET'])
@require_http_methods(['POST'])
def institution_add(request):
    response = {}
    try:
        # institution = Institution(institution_name=request.GET.get('institution_name'))
        institution = Institution(name=request.POST.get('name'))
        institution.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(['GET'])
def institution_list(request):
    response = {}
    try:
        institutions = Institution.objects.filter()
        response['data'] = json.loads(serializers.serialize('json', institutions))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# def institution_list(request):
#     queryset = Institution.objects.all()
#     arr = []
#     for i in queryset:
#         arr.append({
#             'code': Institution.code,
#             'name': Institution.name,
#             'alias': Institution.alias,
#             'province': Institution.province,
#             'city': Institution.city,
#             'area': Institution.area,
#             'address': Institution.address,
#             'institution_type': Institution.institution_type,
#             'institution_property': Institution.institution_property,
#             'institution_character': Institution.institution_character,
#             'post_number': Institution.post_number,
#             'phone': Institution.phone,
#             'approve_status':  Institution.approve_status,
#             'submit_date': Institution.submit_date,
#         })
#     return JsonResponse(arr, safe=False)
