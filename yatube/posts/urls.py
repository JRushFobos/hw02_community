from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('index/', views.index, name='index'),
    # Список групп
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
