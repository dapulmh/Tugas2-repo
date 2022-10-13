from http.client import HTTPResponse
import json
from todolist.models import TaskTodolist
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.forms import TaskForm
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_user = TaskTodolist.objects.filter(user = request.user)
    context = {
        'user_data': data_user,
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
        else:
            messages.success(request, 'Kesalahan dalam penginputan')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task_user(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date = datetime.datetime.now()
            TaskTodolist.objects.create(title = title, description = description, date = date, user = request.user)
            return redirect('todolist:show_todolist')
    else:
        form = TaskForm()

    context = {
        'last_login': request.COOKIES['last_login'],
        "form": form
    }
    return render(request,"create-task.html", context)

@login_required(login_url='/todolist/login/')
def finish_user(request, id):
    task = TaskTodolist.objects.get(id=id)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_user(request, id):
    task = TaskTodolist.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def show_json(request):
    data = TaskTodolist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    data_user = TaskTodolist.objects.filter(user = request.user)
    context = {
        'user_data': data_user,
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method == "POST":
        user = request.user
        date = datetime.date.today()
        title = request.POST.get('title')
        description = request.POST.get('description')  
        is_finished = False   
        new_task = TaskTodolist(user = user, date = date, title = title, description = description, is_finished = is_finished)
        new_task.save()  
        return JsonResponse({
            'user' : new_task.id,
            'date' : date,
            'title' : title,
            'description' : description,
            'is_finished' : is_finished
        })
