from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_address = models.TextField(null=True, blank=True)
    pincode = models.CharField(max_length=6,null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics/',null=True, blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
    
class Address(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=50, default='Home')
    phone_number = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    full_address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    landmark = models.CharField(max_length=100, blank=True)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.full_address[:30]}"