from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('add_task/<str:user_id>/',views.addtask, name="addtask"),
    path('update_task/<int:pk>/<int:task_id>/',views.updatetask, name="updatetask"),
    path('delete/<str:task_id>/', views.delete, name="delete"),

]