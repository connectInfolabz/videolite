from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    added_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

