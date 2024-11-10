from django.shortcuts import render, HttpResponseRedirect
from .models import Task
from users.models import User


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'tasks/base.html', context)


def tasks(request):
    all_tasks = Task.objects.all()
    all_tasks = all_tasks.filter(user=request.user)
    context = {'all_tasks': all_tasks,
               'title': 'Мои задачи'}
    return render(request, 'tasks/tasks.html', context)


def add_task(request):
    user = request.user
    title = request.POST['title']
    description = request.POST['description']
    Task.objects.create(user=user, title=title, description=description)
    return HttpResponseRedirect('/tasks/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/tasks/')
