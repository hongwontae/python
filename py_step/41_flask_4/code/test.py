import requests;

data = requests.get(url = 'https://api.npoint.io/c790b4d5cab58020d391').json()

for blog_post in data :
    if blog_post['id'] == 2 :
        print(blog_post['title'])
        print(blog_post['id'])
        print(type(blog_post['id']))
        print(blog_post['subtitle'])

