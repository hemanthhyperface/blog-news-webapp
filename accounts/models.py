from django.conf import settings
from django.db import models
from django.utils import timezone
from blog.models import Post
from django.contrib.auth.models import User


class UserInfo(models.Model):
    technology = 'tc'
    sports = 'sp'
    philosophy = 'ph'
    politics = 'pl'

    cat_choices = (
        (technology, 'technology'),
        (sports, 'sports'),
        (philosophy, 'philosophy'),
        (politics, 'politics'),
    )
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
  
    fullname= models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=50, )
    password2 = models.CharField(max_length=50)

    preferred_category = models.CharField(max_length=200, choices=cat_choices)
    profile_photo = models.ImageField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.fullname

   

    
