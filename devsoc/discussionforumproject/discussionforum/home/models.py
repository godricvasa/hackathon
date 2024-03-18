from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.username
