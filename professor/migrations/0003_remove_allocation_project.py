# Generated by Django 4.2.5 on 2024-03-28 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_allocation_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='project',
        ),
    ]
