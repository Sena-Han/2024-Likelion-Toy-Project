from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodolistForm
from .models import Todolist

def todolist(request):
    todolists = Todolist.objects.filter(author=request.user, completed=False)
    return render(request, 'todolist.html', {'todolists': todolists})

def tododetail(request, pk):
    todolist = get_object_or_404(Todolist, id=pk, author=request.user)
    return render(request, 'tododetail.html', {'todolist': todolist})

def todopost(request):
    if request.method == "POST":
        form = TodolistForm(request.POST)
        
        if form.is_valid():
            todolist = form.save(commit=False)
            todolist.author = request.user
            todolist.save()
            return redirect('todolist')
    else:
        form = TodolistForm()
    return render(request, 'todopost.html', {'form': form})

def todoedit(request, pk):
    todolist = get_object_or_404(Todolist, id=pk, author=request.user)

    if request.method == "POST":
        form = TodolistForm(request.POST, instance=todolist)

        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = TodolistForm(instance=todolist)
    return render(request, 'todopost.html', {'form': form})

def tododone(request, pk):
    todolist = get_object_or_404(Todolist, id=pk, author=request.user)
    todolist.completed = True
    todolist.save()
    return redirect('todolist')

def tododonelist(request):
    dones = Todolist.objects.filter(author=request.user, completed=True)
    return render(request, 'tododonelist.html', {'dones': dones})