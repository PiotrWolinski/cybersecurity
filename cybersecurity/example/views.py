from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

def index(request):
    items = Todo.objects.order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    form = TodoForm()

    page = {
        'forms' : form,
        'list' : items,
        'title' : "Todo-list",
    }

    return render(request, 'example/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')