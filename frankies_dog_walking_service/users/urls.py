from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name = 'login'),
    path('review/', views.review, name = 'review'),
    path('book/', views.book, name = 'book'),  

]