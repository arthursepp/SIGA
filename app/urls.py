
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]

