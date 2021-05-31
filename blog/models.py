from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
      title=models.CharField(max_length=100)
      content=models.TextField()
      TAG_CHOICES = [
            ('misc','Miscellaneous'),
            ('fash', 'Fashion'),
            ('food','Food'),
            ('life','Lifestyle'),
            ('music','Music'),
            ('sports','Sports'),
            ('health','Health'),
            ('edu','Education'),
            ('softw','Software'),
            ('tech','Technology'),
            ('fit','Fitness'),
            ('crypto','Cryptocurrency'),
            ('travel','Travel'),
            ('pd','Personality Development'),
            ('med','Medicine'),
      ]
      tag = models.CharField(max_length=6, choices=TAG_CHOICES, default='misc')
      date_posted=models.DateTimeField(default=timezone.now)
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      
def __str__(self):
      return self.title