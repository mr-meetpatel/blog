from django.urls import path
from . import views
from .views import UserRegisterView
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout')
]