from django.shortcuts import render , redirect
from .models import Task
from django.db import connection
# Create your views here.

def home(request):
    data = Task.objects.all()
    return render(request, 'Home.html',{"data":data})

def get_task(request):
    data = Task.objects.all()
    return render(request,'get.html',{"data":data})

def create(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        print(task_name)
        if task_name:
            Task.objects.create(task_name=task_name)
            data = Task.objects.all()
            return render(request,"home.html",{"data":data})
    return render(request,"home.html")

def delete_task(request,id):
    object = Task.objects.get(id=id)
    object.delete()
    if not Task.objects.all():
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE app_task AUTO_INCREMENT = 1")        
    data = Task.objects.all()
    return render(request,"home.html",{"data":data})
            
def update_task(request,id):
    data = Task.objects.get(id=id)
    if request.method == "POST":
        data.task_name = request.POST['task_name']
        data.save()
        return redirect('home')   
    return render(request,'update.html',{"data":data})
        
    