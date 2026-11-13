from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("user", "User"),
        ("manager", "Manager"),
        ("supervisor", "Supervisor"),
        ("superadmin", "Super_Admin"),
    ]
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    img = models.ImageField(upload_to="user_images/", null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now, editable=True)

    def __str__(self):
        return self.username
