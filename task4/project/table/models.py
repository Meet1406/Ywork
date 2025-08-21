
from djongo import models

# Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name


# Leave Application model
class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    month = models.PositiveIntegerField()  # 1 = Jan, 2 = Feb, etc.
    year = models.PositiveIntegerField()
    leave_count = models.PositiveIntegerField(default=0)

    def calculate_payable_salary(self):
        # Deduction = base_salary / 25 per leave
        deduction = (self.employee.base_salary / 25) * self.leave_count
        return self.employee.base_salary - deduction

    def __str__(self):
        return f"{self.employee.name} - {self.month}/{self.year}"

# Create your models here.