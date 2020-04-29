from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.forms import ProfileForm, SignUpForm
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request= request, template_name= 'users/signup.html', context={'form':form})



@login_required
def update_profile(request):
    # form validation
    profile = request.user.userprofile

    if request.method == 'POST':
        print(request.FILES)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
            profile.website = data['website']
            profile.phone_number = data['website']
            profile.bio = data['bio']
            profile.profile_pic = data['profile_pic']
            profile.save()

            return redirect('update_profile')            
    else:
        form = ProfileForm()

    return render(
        request=request, 
        template_name='users/update_profile.html',
        context = {
            'profile': profile,
            'user':request.user,
            'form': form,
        })

