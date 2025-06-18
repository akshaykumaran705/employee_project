from rest_framework import viewsets, filters
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Department
from django.db.models import Count

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['date_of_joining', 'name']

@api_view(['GET'])
def employees_per_department(request):
    data = Department.objects.annotate(emp_count=Count('employee')).values('name', 'emp_count')
    return Response(data)