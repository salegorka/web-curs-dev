from django.db import models

# Create your models here.

class Post(models.Model):
    """

    Модель представляющая посты на форуме

    """

    text = models.TextField(max_length=1000, help_text="Сообщение на форуме")
    date = models.DateField()
    author = 0;
    theme = 0;

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return 'Сообщение %s (%s)' % (self.author, self.date)

class Theme(models.Model):
    """

    Модель представляющая тему на форуме

    """
    name = models.CharField(max_length=100, help_text="Тема на форуме")

    def __str__(self):
        return "Тема %s" % (self.name)

class ParentTheme(models.Model):
    """

    Модель представляющая форму родителя

    """
    parent_theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    child_theme = models.ForeignKey('Theme', on_delete=models.CASCADE)

    def __str__(self):
        return "Связь сообщений %s %s" % (self.parent_theme.name, self.child_theme.name)