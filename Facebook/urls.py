from django.urls import path
from . import views


urlpatterns = [
    path('', views.facebook, name="facebook"),
    path('login', views.newLogin, name="login"),
    path('post', views.post, name="post"),
]
