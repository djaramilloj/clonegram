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
            profile = request.user.UserProfile
            if not profile.profile_pic or not profile.bio:
                if request.path not in [reverse('update_profile'), reverse('logout') ]:
                    return redirect('update_profile')
        
        response = self.get_response(request)
        return response


