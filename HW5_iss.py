# http://open-notify.org/Open-Notify-API/ISS-Location-Now/ - ISS
# показать в какой точке мира находится станция сейчас. 
import urllib.request
import urllib.error
import json


def get_iss_position(url):
    iss = 'iss_position'
    lat = 'latitude'
    long = 'longitude'
    try:
        res = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print('Не удалось связаться с сервером. Проверьте подключение к интернету.')
    else:
        obj = json.loads(res.read())
        print('Текущее местоположение МКС {}Широта: {} Долгота: {}'.format('\n', obj[iss][lat], obj[iss][long]))


if __name__ == '__main__':
    url = 'http://api.open-notify.org/iss-now.json'
    get_iss_position(url)
