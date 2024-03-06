from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout_page", views.logout_page, name="logout_page"),
]
