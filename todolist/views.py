from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist = Task.objects.filter(user=request.user)
    context = {
        'name' : 'Maureen Esther Wijaya',
        'npm' : '2106705335',
        'last_login': request.COOKIES.get('last_login', ""),
        'todolist' : todolist
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description, user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request, "create_task.html")

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_task(request):
    print("hi")
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Task.objects.create(title=title, description=description, user=request.user)
        # response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        task = Task.objects.create(title=title, description=description, user=request.user)
        print(task.date)
        return JsonResponse(
            {
                "pk": task.pk,
                "fields": {
                    "date": task.date,
                    "title": task.title,
                    "description": task.description,
                },
            }
        )

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been successfully created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Incorrect Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response