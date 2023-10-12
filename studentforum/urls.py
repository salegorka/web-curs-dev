from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("accounts/reg", views.reg, name="reg"),
    path("question", views.question, name="question")
]
