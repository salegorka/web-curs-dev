from django.db import models
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    """
    
    Группа
    
    """
    name = models.CharField(max_length=30, help_text="Название группы")
    STUDY_FORM_CHOICES = [
        ("ochno", "очная"),
        ("zaochno", "заочная"),
        ("vecher", "вечерняя")
    ]
    study_form = models.CharField(max_length=7, choices=STUDY_FORM_CHOICES, default=STUDY_FORM_CHOICES[0])
    year = models.IntegerField(default=1, help_text="Год обучения")


class Student(models.Model):
    """

    Студент

    """
    first_name = models.CharField(max_length=20, help_text="Имя студента")
    surname = models.CharField(max_length=30, help_text="Фамилия студента")
    father_name = models.CharField(max_length=30, help_text="Отчество студента")
    group = models.ForeignKey(Group, on_delete=models.PROTECT, help_text="Группа")
    number = models.IntegerField(help_text="Номер студенческого")
    PAYMENT_FORM_CHOICES = [
        ("goverment", "бюджетная"),
        ("personal", "платная")
    ]
    payment_form = models.CharField(max_length=9, choices=PAYMENT_FORM_CHOICES, default=PAYMENT_FORM_CHOICES[0])
    document = models.CharField(max_length=70, default="Приказ о зачислении №1111/у от 04.08.2014")


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
    type = models.CharField(max_length=100, help_text="Тип справки", default="Справка о том, что является студентом")

    def get_absolute_url(self):
        return reverse("req-detail", kwargs={"pk": self.pk})
    