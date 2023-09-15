from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Theme(models.Model):
    """

    Модель представляющая тему на форуме

    """
    name = models.CharField(max_length=100, help_text="Тема на форуме")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Post(models.Model):
    """

    Модель представляющая посты на форуме

    """

    text = models.TextField(max_length=1000, help_text="Сообщение на форуме")
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return 'Сообщение %s (%s)' % (self.author, self.date)

class ParentTheme(models.Model):
    """

    Модель представляющая форму родителя

    """
    parent_theme = models.ForeignKey('Theme', on_delete=models.PROTECT)
    child_theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    def __str__(self):
        return "Связь сообщений %s %s" % (self.parent_theme.name, self.child_theme.name)