from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def todo_list(request):
    items = ToDo.objects.filter(complete=False)
    context = {
        'todo_list': items, 
    }
    return render(request, 'todo/todo_list.html', context)

def todo_detail(request, pk):
    item = ToDo.objects.get(pk=pk)
    context = {
        'todo': item,
    }
    return render(request, 'todo/todo_detail.html', context)

def todo_post(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_detail', todo.pk)
    else:
        form = ToDoForm()
        context = {
            'form': form,
        }
        return render(request, 'todo/todo_post.html', context)

def todo_edit(request, pk):
    todo = ToDo.objects.get(pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_detail', pk)
    else:
        form = ToDoForm(instance=todo)
        context = {'form': form}
        return render(request, 'todo/todo_edit.html', context)

def todo_delete(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo:todo_list')

def done_list(request):
    items = ToDo.objects.filter(complete=True)
    context = {
        'done_list': items,
    }
    return render(request, 'todo/done_list.html', context)

def done(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')
