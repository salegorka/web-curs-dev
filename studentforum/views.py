from django.shortcuts import render
from django.views import generic
from .models import Req 

# Create your views here.
def index(request):
    """
    
    Функция для отображения домашней страницы

    """
    return render(
        request,
        "index.html"
    )

def logout_page(request):
    """
    
    Функция для отображения страницы выхода с сайта
    
    """
    return render(
        request,
        "registration/logout.html"
    )


class ReqListView(generic.ListView):
    model = Req