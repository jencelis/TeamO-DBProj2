from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

class Instructor(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='dept_name', blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'instructor'

class Funding(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.CharField(max_length=4)

    class Meta:
        db_table = 'funding'

class Publication(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year_published = models.CharField(max_length=4)

    class Meta:
        db_table = 'publication'

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=255)
    dept_name = models.CharField(max_length=50)  # Assuming department names are short strings
    credits = models.IntegerField()

    class Meta:
        db_table = 'course'  # Ensure this matches the actual table name in your database

    def __str__(self):
        return f"{self.title} ({self.course_id})"

class Section(models.Model):
    course = models.OneToOneField(Course, on_delete=models.DO_NOTHING, primary_key=True)
    sec_id = models.CharField(max_length=4)
    semester = models.IntegerField()
    year = models.IntegerField()
    building = models.CharField(max_length=32, blank=True, null=True)
    room = models.CharField(max_length=8, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)
