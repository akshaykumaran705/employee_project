from rest_framework import viewsets, filters
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from employees.models import Department, Employee
import json

# --- Monthly Attendance Summary (API JSON) ---
@api_view(['GET'])
def monthly_attendance(request):
    data = (
        Attendance.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(present_count=Count('id'))
        .order_by('month')
    )

    # Convert month to string for readability
    for item in data:
        if item['month']:
            item['month'] = item['month'].strftime('%b %Y')

    return Response(data)


# --- Attendance CRUD API ---
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['employee', 'date']
    search_fields = ['status']
    ordering_fields = ['date']


# --- Performance CRUD API ---
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['employee', 'rating']
    search_fields = ['comments']
    ordering_fields = ['review_date']


# --- Combined Charts View (HTML Page) ---
from django.shortcuts import render
from employees.models import Employee
from attendance.models import Attendance
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json

def charts_view(request):
    department_data = list(
        Employee.objects
        .values('department__name')
        .annotate(count=Count('id'))
    )

    attendance_data = list(
        Attendance.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    # Debug: Print data to terminal
    print("🟢 Department Data:", department_data)
    print("🟢 Attendance Data:", attendance_data)

    # Fix month format
    for item in attendance_data:
        if item['month']:
            item['month'] = item['month'].strftime('%b %Y')

    return render(request, 'charts.html', {
        'department_data': json.dumps(department_data),
        'attendance_data': json.dumps(attendance_data),
    })


