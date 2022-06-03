from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pic = models.ImageField(upload_to="usr/%y")
    comment = models.TextField()
    point = models.IntegerField(default=0)

    # pip install pillow
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"