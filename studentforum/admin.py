from django.contrib import admin
from .models import Student, Group, Req, Status

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Req)
admin.site.register(Status)

