from django.core.management.base import BaseCommand
from employees.models import Employee, Department
from attendance.models import Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake employees, attendance, and performance data'

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
        dept_objs = [Department.objects.get_or_create(name=dept)[0] for dept in departments]

        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:15],
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-3y', end_date='today'),
                department=random.choice(dept_objs)
            )
            employees.append(emp)
        
        for emp in employees:
            used_dates = set()
            while len(used_dates) < 10:
                random_date = fake.date_between(start_date='-1y', end_date='today')
                if random_date not in used_dates:
                    used_dates.add(random_date)
                    Attendance.objects.create(
                        employee=emp,
                        date=random_date,
                        status=random.choice(['Present', 'Absent', 'Late'])
                    )


            for _ in range(2):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS('✅ Seeded 50 employees with attendance and performance data.'))
