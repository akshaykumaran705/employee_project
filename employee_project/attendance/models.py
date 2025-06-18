from django.db import models
from employees.models import Employee


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')  # Optional: Prevent duplicate entries per employee per day

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"


class Performance(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating} on {self.review_date}"
