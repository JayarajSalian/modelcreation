from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_No=models.IntegerField(primary_key=True)
    Emp_Name=models.CharField(max_length=100)
    Dept_no=models.IntegerField()

    def __str__(self):
        return self.Employee
class Department(models.Model):
    Dept_No=models.OneToOneField(Employee,on_delete=models.CASCADE)
    Dept_Location=models.CharField(max_length=100)
    def __str__(self):
        return self.Dept_Location