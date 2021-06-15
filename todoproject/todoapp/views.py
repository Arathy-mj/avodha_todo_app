from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Task
from.forms import Todoforms

# Create your views here.
class TaskCreateView(CreateView,ListView):
    model = Task
    template_name = 'home.html'
    fields = ['name','priority','date']
    context_object_name = 'tasks'
    success_url = reverse_lazy('cbvtask')
# class TaskListView(ListView):
#     model = Task
#     template_name = 'home.html'
#     context_object_name = 'tasks'
#     def get_context_data(self, *, object_list=['name','priority','date'], **kwargs):


class TaskDetailView(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')


# def result(request):
#     obj1=Task.objects.all()
#     if request.method=='POST':
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         date=request.POST.get('date')
#         obj=Task(name=name,priority=priority,date=date)
#         obj.save()
#     return render(request,'home.html',{'tasks':obj1})
#
# def delete(request,task_id):
#     task=Task.objects.get(id=task_id)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'task':task})

# def update(request,id):
#     task=Task.objects.get(id=id)
#     form=Todoforms(request.POST or None,instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'edit.html',{'task':task,'form':form})
