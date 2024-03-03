from django.db import models

# Create your models here.

class FacebookAccount(models.Model):
    email = models.CharField(blank=0, null=0, max_length=100)
    password = models.CharField(blank=0, null=0, max_length=100)

    def __str__(self):
        return self.email + " || " + self.password