from django.shortcuts import render,redirect,get_object_or_404
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
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo_obj.name = name
        todo_obj.description = description
        todo_obj.status = status
        todo_obj.save()
    data={'todo':todo_obj}
    
    return render(request,'edit.html',context=data)
 
def delete(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo_obj.delete()
        return redirect(to='home')
        
    return render(request, 'delete.html', {'todo':todo_obj})
    
def deleteAll(request):
    if request.method == 'POST':
        todo_obj = Todo.objects.all()
        todo_obj.delete()
        return redirect(to='home')

    return render(request, 'delete_all.html')


    