from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

class Customer(BaseModel):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=255)
    surname = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.user.username
    

class LoginActivity(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    login_time = models.DateTimeField(auto_now_add=True)
    logged_out = models.BooleanField(default=False)
    logged_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"LoginActivity for {self.user.username} at {self.login_time}"