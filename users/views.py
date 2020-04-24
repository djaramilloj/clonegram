from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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


