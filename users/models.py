from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True,max_length=254)
    about = models.TextField(blank=True, null=True)
    
    def __str__(self):
        if len(self.name) != 0:
            return self.name
        return self.user.username
    
    