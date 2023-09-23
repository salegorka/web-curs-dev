from django.shortcuts import render

# Create your views here.
def index(request):
    """
    
    Функция для отображения домашней страницы

    """

    return render(
        request,
        "index.html"
    )
