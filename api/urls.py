from django.urls import path
from . import views
from . views import *
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path


urlpatterns = [
    path('', views.TodoCompletedList.as_view()),
    path('<int:pk>/', views.ToDoDetail.as_view()), 
    path('register/', RegisterAPI.as_view(), name='Register'),
    path('login/', LoginAPI.as_view(), name='Login'),
    path('logout/', knox_views.LogoutView.as_view(), name='Logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='Logoutall'),
   
]
