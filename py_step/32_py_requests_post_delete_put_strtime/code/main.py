import requests
import datetime

pixela_api_endpoint = "https://pixe.la/v1/users"
TOKEN = 'k2xkoala3121je2'
USER_NAME = 'alister' 
GRAPH_HEADER = {
    'X-USER-TOKEN' : TOKEN
}
USER_ID = 'graph66'

today = datetime.datetime(year=2024, month=11, day=29).strftime('%Y%m%d')
print(today)



pixela_post_data = {
    'date' : today,
    'quantity' : '9.74'
}


response = requests.post(url=f'{pixela_api_endpoint}/{USER_NAME}/graphs/{USER_ID}'
                         ,headers= GRAPH_HEADER, json=pixela_post_data)
response.raise_for_status()
data = response.json()
print(data)

# pixela_body = {
#     'token' : 'k2xkoala3121je2',
#     'username' : 'alister',
#     "agreeTermsOfService" : 'yes',
#     "notMinor" : 'yes'
# }

# response = requests.post(url=pixela_api_endpoint,json=pixela_body)
# response.raise_for_status()
# data = response.json()
# print(data)

# update_body = {
#     'id': 'graph66',
#     'name' : 'Book Record',
#     'unit' : 'Km',
#     'type' : 'float',
#     'color' : 'ajisai'
# }

# response = requests.post(url=f'{pixela_api_endpoint}/{USER_NAME}/graphs', json=update_body, headers=graph_header)
# response.raise_for_status()
# data = response.json()
# print(data)
