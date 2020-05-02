
"""Users views."""

# Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, UpdateView
from users.forms import SignUpForm

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import UserProfile

# Forms
from users.forms import SignUpForm



class SignUpView(FormView):
    template_name= 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    # Form_valid should always be recalled when using FormViews of django in order to make the logic of the form works
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/details.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name='users/update_profile.html'
    model = UserProfile
    fields = ['website', 'bio', 'phone_number', 'profile_pic']

    def get_object(self):
        # return user's profile
        return self.request.user.userprofile
    
    def get_success_url(self):
        # return to user's profile
 
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})



class LoginView(auth_views.LoginView):
    template_name='users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name='users/logged_out.html'