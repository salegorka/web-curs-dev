from django.db import models


# Create your models here.
class Group(models.Model):
    """
    
    Группа
    
    """
    name = models.CharField(max_length=30, help_text="Название группы")


class Student(models.Model):
    """

    Студент

    """
    first_name = models.CharField(max_length=20, help_text="Имя студента")
    surname = models.CharField(max_length=30, help_text="Фамилия студента")
    father_name = models.CharField(max_length=30, help_text="Отчество студента")
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    number = models.IntegerField()


class Req(models.Model):
    """
    
    Заявка на справку, содержит пока только ссылку на студента
    
    """
    student = models.ForeignKey(Student, on_delete=models.PROTECT)