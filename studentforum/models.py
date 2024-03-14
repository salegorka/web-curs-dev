from django.db import models
from django.urls import reverse

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

class Status(models.Model):
    """
    
    Статус заявки
    
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, help_text="Название статуса")

class Req(models.Model):
    """
    
    Заявка на справку
    
    """
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=1)

    def get_absolute_url(self):
        return reverse("req-detail", kwargs={"pk": self.pk})
    