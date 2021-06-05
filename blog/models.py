from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
      title=models.CharField(max_length=100)
      content=models.TextField()
      TAG_CHOICES = [
            ('Miscellaneous','Miscellaneous'),
            ('Fashion', 'Fashion'),
            ('Food','Food'),
            ('Lifestyle','Lifestyle'),
            ('Music','Music'),
            ('Sports','Sports'),
            ('Health','Health'),
            ('Education','Education'),
            ('Software','Software'),
            ('Technology','Technology'),
            ('Fitness','Fitness'),
            ('Cryptocurrency','Cryptocurrency'),
            ('Travel','Travel'),
            ('Personality Development','Personality Development'),
            ('Medicine','Medicine'),
            ('Entertainment','Entertainment'),
      ]
      tag = models.CharField(max_length=25, choices=TAG_CHOICES, default='misc')
      date_posted=models.DateTimeField(default=timezone.now)
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      
      def __str__(self):
        return self.title
      
      def get_absolute_url(self):
            return reverse('post-detail',kwargs={'pk':self.pk})