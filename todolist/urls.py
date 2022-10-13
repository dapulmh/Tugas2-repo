from django.urls import path
from todolist.views import add_task_ajax, show_json, show_todolist, show_todolist_ajax
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import register
from todolist.views import create_task_user
from todolist.views import finish_user
from todolist.views import delete_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task_user, name='create-task'),
    path('finish/<int:id>', finish_user, name='finish_user'),
    path('delete/<int:id>', delete_user, name='delete_user'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task_ajax, name='add_task_ajax')
]