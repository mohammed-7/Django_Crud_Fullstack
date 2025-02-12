from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path("get",views.get_task,name='get_task'),
    path("update/<int:id>/",views.update_task,name='update_task'),

]
