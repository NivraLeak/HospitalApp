from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def get_full_name(self):
        return  '{} {}'.format(self.first_name,self.last_name)

class MedicalStaff(User):
    class Meta:
        proxy = True

    def get_resources(self):
        return [ ]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    lastName = models.TextField()
    typePersonal = models.TextField()
