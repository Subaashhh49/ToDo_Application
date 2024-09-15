from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos' : todo_objs}

    return render(request, 'index.html',context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status)    
    return render(request,'create.html')


def edit(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    if request.method == 'POST':
        name =  request.POST.get('name')
        description =  request.POST.get('description')
        status =  request.POST.get('status')
        todo_obj.name = name
        todo_obj.description = description
        todo_obj.status = status
        todo_obj.save()
    data = {'todo':todo_obj}
    return render(request,'edit.html',context=data)

