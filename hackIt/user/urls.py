from django.urls import path
from . import views

urlpatterns = [
    #path('login',views.user_login,name='login'),
    path('register',views.register_user,name="register"),
]