import requests;
import bs4;

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
response.raise_for_status()
movie_data = response.text

# list_title = []

html_movie_100 = bs4.BeautifulSoup(movie_data, 'html.parser')
title_list_data = html_movie_100.find_all('h3', class_='title')

# for data in title_list_data :
#     tt = data.getText()
#     list_title.append(tt+'\n')

list_title = [tt.getText() for tt in title_list_data]

movies = list_title[::-1]

with open('./movie.txt', 'w', encoding='utf-8') as file :
    for tc in movies :
        file.write(tc+'\n')
