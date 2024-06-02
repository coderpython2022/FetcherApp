from django.http import HttpResponse
from django.conf import settings
import ipinfo, requests


ipp = requests.get('https://api64.ipify.org?format=json').json()

def get_ip_details(ip_address=None):
	ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
	ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
	ip_data = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
	ip_data = ip_data.getDetails(ip_address)
	return ip_data

def location(request):
	
	ip_data = get_ip_details(ipp['ip'])
	response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}.'.format(ip_data.ip,ip_data.loc,ip_data.city)
	return HttpResponse(response_string)

get_ip_details(ipp['ip'])