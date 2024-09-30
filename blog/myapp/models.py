from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 100, blank= True)
    body = models.TextField(max_length=500)
    date_posted = models.DateField()
    
    def _str_(self):
        return self.title
