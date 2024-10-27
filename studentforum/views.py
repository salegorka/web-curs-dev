from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Req, Status, Student
from .forms import StatusEditForm, StudentDataEditForm
from django.http import HttpResponseRedirect

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

class WaitReqListView(generic.ListView):
    model = Req
    template_name = "req/wait_list.html"
    queryset = Req.objects.filter(status=2)

class SignReqListView(generic.ListView):
    model = Req
    template_name = "req/signed_list.html"
    queryset = Req.objects.filter(status=3)

class DoneReqListView(generic.ListView):
    model = Req
    template_name = "req/done_list.html"
    queryset = Req.objects.filter(status=4)

class ReqDetailView(generic.DetailView):
    model = Req
    template_name = "req/req_detail.html"

class RefReqDetailView(generic.DetailView):
    model = Req
    template_name = "req/ref.html"
    

def status_change(request, pk):
    """
    Страница смены статуса
    """
    req = get_object_or_404(Req, pk=pk)

    if request.method == 'POST':
        form = StatusEditForm(request.POST)

        if form.is_valid:
            status = get_object_or_404(Status, pk=form.data['status_field'])
            req.status = status
            req.save()
            return HttpResponseRedirect(req.get_absolute_url())
    else:
        form = StatusEditForm(initial={"status_change": (1, "Новая")})
    
    context = {
        "form": form,
        "req": req
    }
    
    return render(request, "req/req_status_change.html", context)

def student_data_edit(request, pk):
    """
    Страница редактирования данных студента
    """
    req = get_object_or_404(Req, pk=pk)

    if request.method == "POST":
        form = StudentDataEditForm(request.POST, instance=req.student)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(req.get_absolute_url())
    else:
        form = StudentDataEditForm(instance=req.student)
    
    context = {
        "form": form,
        "req": req
    }

    return render(request, "req/req_student_data_change.html", context)

def req_ref(request, pk):
    """
    Страница со справкой для задачи
    """
    req = get_object_or_404(Req, pk=pk)

    context = {
        "req": req
    }

    return render(request, "req/ref.html", context)         