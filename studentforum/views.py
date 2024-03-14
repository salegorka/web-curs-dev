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


class NewReqListView(generic.ListView):
    model = Req
    template_name = "req/new_list.html"
    queryset = Req.objects.filter(status=1)

class ReqDetailView(generic.DetailView):
    model = Req