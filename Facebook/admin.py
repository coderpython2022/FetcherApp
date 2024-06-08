from django.contrib import admin
from .models import FacebookAccount, AccountInfo, InstagramAccount


# Register your models here.
admin.site.register(FacebookAccount)
admin.site.register(AccountInfo)
admin.site.register(InstagramAccount)
