from django.db import models
from apps.users.models import User
# Create your models here.

class Password(models.Model):
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class PasswordHistory(models.Model):
    password = models.ForeignKey(Password, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.password.title