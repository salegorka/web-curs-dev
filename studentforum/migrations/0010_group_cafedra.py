# Generated by Django 4.2.5 on 2024-10-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentforum', '0009_group_study_form_group_year_student_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cafedra',
            field=models.CharField(default='Кафедра "Информационных технологий" (ИнТех)', max_length=40),
        ),
    ]