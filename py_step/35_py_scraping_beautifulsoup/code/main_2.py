import requests;
import bs4;

response = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
response.raise_for_status()
page_data = response.text

html_page_data = bs4.BeautifulSoup(page_data, "html.parser")
a_data = html_page_data.find_all('a', class_ = 'storylink')

for da in a_data :
    print(da.get('href'))


