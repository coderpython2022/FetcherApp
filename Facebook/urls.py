from django.urls import path
from . import views, ipinfo


urlpatterns = [
    path('', views.facebook, name="facebook"),
    path('instagram', views.instagram, name="instagram"),
    path('login', views.newLogin, name="login"),
    path('post', views.post, name="post"),
    path('checkIpInfoDetails', ipinfo.checkIpInfoDetails, name="checkIpInfoDetails"),
]
