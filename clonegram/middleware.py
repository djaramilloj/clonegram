# clonegram middleware

# django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:

    # ensure every user has their profile pic and bio
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):

        # cant access to profile for some reason
        if not request.user.is_anonymous:
            if not request.user.is_staff:        
                profile = request.user.userprofile
                if not profile.profile_pic or not profile.bio:
                    if request.path not in [reverse('users:update'), reverse('users:logout') ]:
                        return redirect('users:update')
        
        response = self.get_response(request)
        return response


