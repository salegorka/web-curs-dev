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

def profile(request):
    """
    
    Функция для отображения профиля пользователя
    
    """
    return render(
        request,
        "profile.html"
    )

from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

def reg(request):
    """
    
    Функция для отображения страницы регистрации
    
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            guest_group = Group.objects.get(name="Guest")
            guest_group.user_set.add(new_user)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/reg_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/reg.html', {'user_form': user_form})

def question(request):
    """
    
    Функция для отображения страницы с вопросами пользователей
    
    """    
    return render(request, 'question.html')