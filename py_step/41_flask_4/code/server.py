from flask import Flask, render_template;
import random;
import datetime;
import requests

app = Flask(__name__)

@app.route('/')
def home () :
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name) :
    gender_response = requests.get(url=f'https://api.genderize.io?name={name}')
    gender_data = gender_response.json()
    gender = gender_data['gender']
    return render_template('guess.html', name=name, gender=gender)

@app.route('/blog/<num>')
def get_blog(num) :
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    # 리스트 내 딕셔너리 데이터 == all_posts
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__' :
    app.run(debug=True)
