from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
import sweetify
from video.models import Video
# Create your views here.

def login_page(request):
    return render(request, "login_page.html")

def registration_page(request):
    return render(request, "registration.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        queryset = User.objects.get(email = email)
        password = request.POST['password']
        if queryset:
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request,user)
                sweetify.success(request, 'Login successful')
                return redirect("users:dashboard")
            else:
                sweetify.error(request, "email and password doesn't match!", persistent=':(')
                return render(request, "login_page.html")
    return render(request, "login_page.html")

def register_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            queryset = User.objects.get(email = email)
        except:
            queryset = None
        if queryset is None:
            try:
                user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
                sweetify.success(request, 'Registration successful')
                return render(request, "login_page.html")
            except Exception as e:
                sweetify.error(request, f"{e.args[0]}", persistent=':(')
                return render(request, "registration.html")
        else:
            sweetify.error(request, "Email already exists", persistent=':(')
            return render(request, "registration.html")

    return render(request, "registration.html")

def logout_view(request):
    logout(request)
    return render(request, 'login_page.html')


def dashboard_view(request):
    return render(request, "user_dashboard.html")

def added_videos(request):
    try:
        print(request.user)
        queryset = Video.objects.filter(added_by = request.user)
        print(queryset)
    except:
        queryset = None
        print(queryset)
    return render(request, "added_video_list.html", {"videos":queryset})

    
def test_view(request):
    sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    return redirect('/')
                
                

    

            