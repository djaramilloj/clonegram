from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile
from django.db.utils import IntegrityError
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        
        username = request.POST['username'],
        password = request.POST['password']
        
        user= authenticate(request, username= username[0], password= password)
        
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or passowrd'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



def signup(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_conf =request.POST['password_conf']


        if password != password_conf:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password= password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = UserProfile(user=user)
        profile.save()

        return redirect('login')    

    return render(request, 'users/signup.html')



def update_profile(request):
    return render(request, 'users/update_profile.html')

