# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=64, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


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


class Prereq(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)  # The composite primary key (course_id, preq_id) found, that is not supported. The first column is selected.
    preq = models.ForeignKey(Course, models.DO_NOTHING, related_name='prereq_preq_set')

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'preq'),)
