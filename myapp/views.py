from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')



def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})


# User Login
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def pics(request):
    return render(request,'pictures.html')