import requests;
import datetime;

my_lat = 37.749654
my_lng = 127.032865

parameters ={
    'lat' : my_lat,
    'lng' : my_lng,
    'formatted' : 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])


time_now = datetime.datetime.now()


