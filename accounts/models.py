from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetails(AbstractUser):
    ROLES=[
        ("Doctor","Doctor"),
        ("Patient","Patient")
    ]
    
    profile_pic=models.ImageField(upload_to='profiles/')

    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    role=models.CharField(max_length=10,choices=ROLES)

    def __str__(self):
        return self.username