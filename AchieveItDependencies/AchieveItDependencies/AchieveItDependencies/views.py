from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Personnel, Customers, ProjectId, BusinessField
from .serializers import PersonnelSerializer, CustomersSerializer, ProjectIdSerializer, BusinessFieldSerializer


@api_view(['GET'])
def personnel_list_all(request: HttpRequest):
    personnel = Personnel.objects.all().order_by('user_id')
    serializer = PersonnelSerializer(personnel, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def personnel_by_id(request: HttpRequest):
    try:
        requested_id = request.GET['user_id']
        personnel = Personnel.objects.filter(user_id__exact=requested_id).get()
        serializer = PersonnelSerializer(personnel, many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def personnel_by_name(request: HttpRequest):
    try:
        requested_name = request.GET['user_name']
        personnel = Personnel.objects.filter(user_name__contains=requested_name).get()
        serializer = PersonnelSerializer(personnel, many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def customers_list_all(request: HttpRequest):
    customers = Customers.objects.all().order_by('customer_id')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customers_by_id(request: HttpRequest):
    try:
        requested_id = request.GET['customer_id']
        customers = Customers.objects.filter(customer_id__exact=requested_id)
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def customers_by_coordinator(request: HttpRequest):
    try:
        requested_coordinator_id = request.GET['coordinator_id']
        customers = Customers.objects.filter(referred_coordinator_id__exact=requested_coordinator_id)
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def customers_by_name(request: HttpRequest):
    try:
        requested_name = request.GET['corporation_name']
        customers = Customers.objects.filter(corporation_name__contains=requested_name)
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def project_id_list_all(request: HttpRequest):
    project_id = ProjectId.objects.all().order_by('project_id')
    serializer = ProjectIdSerializer(project_id, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def business_field_list_all(request: HttpRequest):
    business_field = BusinessField.objects.all().order_by('business_field_id')
    serializer = BusinessFieldSerializer(business_field, many=True)
    return Response(serializer.data)
