# Generated by Django 4.2.11 on 2024-05-01 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('credits', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('building', models.CharField(blank=True, max_length=32, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'instructor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('total_credits', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='prof.course')),
                ('sec_id', models.CharField(max_length=4)),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('building', models.CharField(blank=True, max_length=32, null=True)),
                ('room', models.CharField(blank=True, max_length=8, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'section',
                'managed': False,
            },
        ),
    ]
