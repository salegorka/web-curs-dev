# Generated by Django 4.2.5 on 2024-03-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentforum', '0004_group_req_student_remove_parenttheme_child_theme_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='req',
            name='process',
            field=models.BooleanField(default='False'),
        ),
    ]