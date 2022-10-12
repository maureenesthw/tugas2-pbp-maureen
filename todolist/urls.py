from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, show_json, add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
]