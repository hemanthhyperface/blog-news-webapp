from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
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
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    category =models.CharField(max_length=30, choices = cat_choices, blank=False)
    text = models.TextField()
    images = models.ImageField(width_field=50,blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


