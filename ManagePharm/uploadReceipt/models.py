from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receipt_image = models.ImageField(upload_to='temp/', blank=True, null=True)
    
    def __str__(self):
        return f"Receipt of {self.user.username}"