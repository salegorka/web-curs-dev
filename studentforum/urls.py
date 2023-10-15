from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout_page", views.logout_page, name="logout_page"),
    path("profile", views.profile, name="profile"),
    path("accounts/reg", views.reg, name="reg"),
    path("question", views.question, name="question"),
    path("cafedra", views.cafedra, name="cafedra")
]
