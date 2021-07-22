from email.mime import image

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # user라는 객체가 살아졌을때 cascade(종속)도 사라짐.

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True) # CharField > 텍스트
    message = models.CharField(max_length=200, null=True)
