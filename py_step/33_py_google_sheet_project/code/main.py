import requests;
import datetime;

APPLICATION_ID = '85139c97'
APPLICATION_API_KEY = '749b121e61bc0d3fb709126becb42cf5'
URL_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = 'male'
WEIGH = '73'
HEIGHT = '176'
AGE = '26'

API_KEY = '3c249efae3a5a32a6f12b3ee598909c6'
SHEET_ENDPOINT = 'https://api.sheety.co/3c249efae3a5a32a6f12b3ee598909c6/myWorkouts/sheet'

test_data = input('tell me, which exercises you did : \n')

headers = {
    'x-app-id' : APPLICATION_ID,
    'x-app-key' : APPLICATION_API_KEY
}

parameters = {
    'query' : test_data,
    'gender' : GENDER,
    'weight_kg' : WEIGH,
    'height_cm' : HEIGHT,
    'age' : AGE
}

response = requests.post(url=URL_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
print(data)

today_date = datetime.datetime.now().strftime('%d%m%Y')
now_time = datetime.datetime.now().strftime('%X')

for exercise in data["exercises"] :
    sheet_input = {
        "sheet" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

print(sheet_input)
print('---------------------------??????????????')

sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input)
sheet_response.raise_for_status()
print(sheet_response)
