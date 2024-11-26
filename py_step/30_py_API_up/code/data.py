import requests;


response = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')

response_data= response.json()['results']

question_data = response_data