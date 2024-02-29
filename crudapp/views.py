from django.shortcuts import render,redirect,get_object_or_404

from crudapp.form import TaskForm
from crudapp.models import Tasks

# Create your views here.

def task_list(request):
    tasks=Tasks.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})
def task_detail(request,id):
    task=get_object_or_404(Tasks,id=id)
def create_task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=TaskForm()
    return render(request,'task_form.html','task_form.html',{'form':form})
def edit_task(request,id):
    task=get_object_or_404(Tasks,id=id)
    if form.is_valid():
        form.save()

    else:
        form=TaskForm(instance=task)
        return render(request,'task_form.html')
def delete_task(request,id):
    task=get_object_or_404(Tasks,id=id)
    if request.method=='POST':
        task.delete()
        return redirect('')
    return render(request,'task_confir_')


