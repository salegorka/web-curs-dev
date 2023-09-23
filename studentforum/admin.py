from django.contrib import admin

# Register your models here.
from .models import Post, Theme, ParentTheme

admin.site.register(Post)
admin.site.register(Theme)
admin.site.register(ParentTheme)

