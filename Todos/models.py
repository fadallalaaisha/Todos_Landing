from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    complate=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


 