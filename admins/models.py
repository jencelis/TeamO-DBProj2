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
    
class Professor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=100)

class CourseSection(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=9)  # e.g., "2023-2024"
    semester = models.CharField(max_length=10)  # e.g., "Fall"
    students = models.ManyToManyField('Student', through='Enrollment')

class Student(models.Model):
    name = models.CharField(max_length=100)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)

class Funding(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.CharField(max_length=4)

class Publication(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year_published = models.CharField(max_length=4)