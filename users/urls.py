# users urls

from django.urls import path

from users import views

urlpatterns = [
    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/signup/', views.signup, name='signup'),
    path('users/me/profile', views.update_profile, name='update_profile'),
]