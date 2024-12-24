import bs4;
import requests;

headers = {
    'Accept-Language' : "ko-KR,ko;q=0.9",
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get('https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463',
                        headers=headers)

html_data = bs4.BeautifulSoup(response.content, 'lxml')
print(html_data.prettify())

price = html_data.find_all('span')
print(price)
# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)