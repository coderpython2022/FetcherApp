from requests import get
import json
def ipinfo():
    ip = get('https://api.ipify.org').text
    query = get(f'http://ip-api.com/json/{ip}').text

    if ip and query:
        return json.loads(query)
    else:
        pass