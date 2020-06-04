from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        user  = User.objects.get(id=current_user.id)
        task = user.task_set.all()
        context={'task':task}
        return render (request, 'index.html', context)
    else:
        return redirect ('login')

        
    
def register(request):
    if request.method =='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user create")
        else:
             messages.info(request,'Password Not Matched')
             return redirect('register')
        return redirect('login')
    else:
        return render (request, 'register.html')


def login(request):
    if request.method== 'POST':
        username =request.POST['username']
        password =request.POST['password1']

        user =auth.authenticate(username=username,password=password)
        user_id = user.id

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required
def addtask(request,user_id):
    user = User.objects.get(id=user_id)
    tasks = user.task_set.all()
    if request.method == 'POST':
        add =request.POST['task']
        task = user.task_set.create(task=add)
        task.save()
        return redirect('/')
    return render(request,'addtask.html')

@login_required
def updatetask(request,pk,task_id):
    user = request.user
    print(user)
    print(task_id)
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        add =request.POST['task']
        complete =request.POST['complete']
        Task.objects.filter(id=task_id).update(task=add,complete=complete)
        return redirect('/')
    context={
        'task':task
    }
    
    return render(request,'updatetask.html',context)

@login_required
def delete(request, task_id):
    task = Task.objects.all().get(id=task_id)
    task.delete()
    return redirect('/')
