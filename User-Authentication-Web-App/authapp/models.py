from django.db import models
from django.conf import settings
# Create your models here.


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class GraphiCards(models.Model):
    name = models.CharField(max_length=30)
    file_name = models.CharField(default='145',max_length=30)
    Rep = models.FileField(upload_to='authapp/static/authapp/images')
    Quantity = models.IntegerField()
    Price = models.FloatField()
    def __str__(self):
        return self.name



