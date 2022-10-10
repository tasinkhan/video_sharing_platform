from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('login-page/', views.login_page, name = "login_page"),
    path('registration-page/', views.registration_page, name = "registration_page"),
    path('login/', views.login_view, name = "login"),
    path('register/', views.register_view, name = "register"),
    path('logout/', views.logout_view, name = "logout"),
    path('test/', views.test_view, name = "test"),
]