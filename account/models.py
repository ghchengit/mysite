from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return 'user {}'.format(self.username)


# Create your models here.
