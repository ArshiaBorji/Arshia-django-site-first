
import django
from django.shortcuts import render
from .models import *
from .forms import *



# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        if request.POST:
            form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            

    context= {    
        'tasks': tasks,
        'form': form
    }
    return render(request,'mohammad/index.html', context)



