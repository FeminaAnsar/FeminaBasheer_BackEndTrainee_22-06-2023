# Generated by Django 4.1.7 on 2023-06-22 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='classStudent',
            new_name='class_Student',
        ),
    ]
