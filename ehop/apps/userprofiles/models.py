from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Another', 'Another')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICE, default='Another')

    def __str__(self):
        return f'{self.user} {self.first_name} {self.last_name} {self.gender} {self.email} {self.phone_number}'

