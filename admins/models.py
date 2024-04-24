from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name