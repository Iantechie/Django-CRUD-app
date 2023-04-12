
from django.urls import path,include
from . import views


app_name = 'members'

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('update/updaterecord/<int:id>/', views.updaterecord, name='updaterecord'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
