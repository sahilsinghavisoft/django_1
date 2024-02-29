from django.shortcuts import render
from .models import*
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employee,company
from .serializers import EmployeeSerializer,companySerializer
from rest_framework import viewsets


#viewset for employee and company by which we can perform crud operations
class employeeviewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=EmployeeSerializer

class companyviewset(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer



    