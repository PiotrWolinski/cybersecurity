from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('del/<int:item_id>', views.remove, name='del'),
    path('tasks/', views.tasks, name='tasks'),
    path('perms/', views.perms, name='perms'),
    ]