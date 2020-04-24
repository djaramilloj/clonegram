#   Posts models

# django

from django.db import models
from django.contrib.auth.models import User
# todas las clases son un modelo en django

class Post(models.Model):
    # Post model

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)

    title = models.CharField(max_length=225)
    photo = models.ImageField(upload_to = 'posts/photos')
    # metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.user.username)