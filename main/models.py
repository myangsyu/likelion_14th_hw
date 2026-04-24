from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20, blank = True)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.content[:20]
