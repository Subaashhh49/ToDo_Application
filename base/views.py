from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos'  : todo_objs}

    return render(request, 'index.html',context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status)    
    return render(request,'create.html')

