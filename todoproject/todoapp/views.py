from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
class Tasklistview(ListView):
    model = Task
    template_name = 'cbvhome.html'
    context_object_name = 'task'


class Detaildetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Updateupdateview(UpdateView):
    model = Task
    template_name = 'cbvupdate.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Deletedeleteview(DeleteView):
    model = Task
    template_name = 'cbvdelete.html'
    success_url = reverse_lazy('cbvhome')




# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    return render(request,'home.html',{'task':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

# def detail(request):
#
#     return render(request,'detail.html',)

def update(request,id):
    idd=Task.objects.get(id=id)
    task=Todoform(request.POST or None, instance=idd)
    if task.is_valid():
        task.save()
        return redirect('/')
    return render(request,'edit.html',{'id':idd,'task':task})