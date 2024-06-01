from urllib.request import urlopen
from django.conf import settings
from django.shortcuts import render
import ipinfo, requests, re, socket
from Facebook import views

def checkIpInfoDetails(request):
    # title = 'فحص عنوان الآي بي'
    # myExternalIp = None

    # inputIp = None
    # location_data = None
    # ip_info = None
    # open_ports = []

    # if request.method == 'GET' and 'scanOpenPorts' in request.GET:
    #     inputIp = f'{ip1}.{ip2}.{ip3}.{ip4}'
    #     for port in range(1,20+1):
    #         try:
    #             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #                 s.settimeout(0.8)
    #                 s.connect(('156.197.192.112', port))
    #                 open_ports.append(port)
    #         except:
    #             print('Error .........===.........===')
    #     for port in open_ports:
    #         print(f"Port {port} is OPEN on {inputIp}.")



    currIP = views.get_ip()
    ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
    ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
    ip_info = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
    ip_info = ip_info.getDetails(currIP).all

    info = requests.get(f'http://ip-api.com/json/{currIP}/')
    location_data = info.json()
    return location_data

    # if request.method == 'GET' and 'getCurrentIpInfo' in request.GET:
    #     # Start Get External IP
    #     data = str(urlopen('http://checkip.dyndns.com/').read())
    #     myExternalIp = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
    #     # End Get External IP

    #     # Start Get Location
    #     getIp = requests.get('https://api64.ipify.org?format=json').json()
    #     ip_address = getIp["ip"]

    #     info = requests.get('http://ip-api.com/json/')
    #     test = requests.get('https://ipinfo.io/json?token=$TOKEN')
    #     location_data = info.json()
    #     # End Get Location

    #     ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
    #     ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
    #     ip_info = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
    #     ip_info = ip_info.getDetails(ip_address).all
    #     ipError = False

    # context = {'title':title,'inputIp':inputIp, 'ip1':ip1, 'ip2':ip2, 'ip3':ip3, 'ip4':ip4, 'myExternalIp':myExternalIp, 'location_data':location_data, 'ip_info':ip_info, 'ipError':ipError, 'errorMsg':errorMsg}
    # return render(request, 'partials/ipInfo.html', context)