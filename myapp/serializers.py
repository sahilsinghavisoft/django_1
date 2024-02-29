from rest_framework import serializers
from .models import employee,company

#serializer for employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
#serializer for company
class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'  # You can also specify the fields explicitly if needed
