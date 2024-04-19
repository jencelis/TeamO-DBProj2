from django.db import models



class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=32)
    building = models.CharField(max_length=32, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Instructor(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'
