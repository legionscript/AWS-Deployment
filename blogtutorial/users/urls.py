from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
]