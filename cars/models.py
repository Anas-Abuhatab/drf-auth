from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=32)
    description = models.TextField()
    manufacturer = models.CharField(max_length=32)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.model