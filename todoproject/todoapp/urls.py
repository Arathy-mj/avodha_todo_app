from django.urls import path
from . import views

urlpatterns = [

    # path('', views.result,name='result'),
    path('', views.TaskCreateView.as_view(), name='cbvtask'),
    # path('',views.TaskListView.as_view(),name='cbvtask'),
    path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),

    # path('delete/<int:task_id>/',views.delete,name='delete'),
    # path('update/<int:id>/',views.update,name='update'),


]
