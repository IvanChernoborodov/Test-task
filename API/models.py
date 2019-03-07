from django.db import models

# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=1000)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.title)