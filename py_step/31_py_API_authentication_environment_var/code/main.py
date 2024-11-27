import requests

API_KEY = '7acef0115123929bb93b17a82696b9d7'
MY_LAT = 37.568291
MY_LNG = 126.997780

request_parameter = {
    'lat' : MY_LAT,
    'lon' : MY_LNG,
    'appid' : API_KEY
}

response = requests.get(url=
    'https://pro.openweathermap.org/data/2.5/forecast/hourly', params=request_parameter)
response.raise_for_status()
data = response.json()
 