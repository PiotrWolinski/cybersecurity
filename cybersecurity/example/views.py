from django.http.request import RAISE_ERROR
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

from .forms import TodoForm
from .models import Todo

def index(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    return render(request, 'example/index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'example/login.html', {'form': form})

    if request.method == 'POST':
        form1 = AuthenticationForm(data=request.POST)
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
                
        else:
            return render(request, 'example/login.html', {'form': form1})


    return redirect('login_view')

def register(request):
    if request.user.is_authenticated:   
        return redirect('tasks')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_group = Group.objects.get(name='User')
            user.groups.add(user_group)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'example/register.html', {'form': form})

@login_required(login_url='index')
def logout_request(request):
    logout(request)

    return redirect('index')

@login_required(login_url='index')
def tasks(request):
    items = Todo.objects.order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    
    form = TodoForm()

    page = {
        'forms' : form,
        'list' : items,
        'title' : "Todo-list",
    }

    return render(request, 'example/tasks.html', page)

@permission_required('example.can_enter_admin_panel', login_url='index', raise_exception=True)
def perms(request):
    return render(request, 'example/perms.html')

@permission_required('example.delete_todo', login_url='index')
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('tasks')