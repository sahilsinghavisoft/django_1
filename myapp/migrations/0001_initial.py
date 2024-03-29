# Generated by Django 5.0.2 on 2024-02-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('HR', 'HR')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ID', models.IntegerField(default=0)),
                ('employee_role', models.CharField(max_length=50)),
                ('employee_salary', models.IntegerField(default=0)),
            ],
        ),
    ]
