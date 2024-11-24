# import smtplib;

my_email = "kongwontae@gmail.com"
password = "rnyp yyzv ambp qwzn"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection :
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#     from_addr=my_email, to_addrs="dnjsxoghd@naver.com", msg="Subject:Hello\n\n This is body of my email")

import datetime as dt
import random
import smtplib

# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week) # 일요일 => 6
# my_birthday = dt.datetime(year=1998, month=2, day=23)
# print(my_birthday)
today_of_week_num = dt.datetime.now().weekday()

if today_of_week_num == 6 :
    with open('./quotes.txt') as q_file :
        data = q_file.readlines()
        random_quote = random.choice(data)
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection :
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='dnjsxoghd@naver.com'
                            , msg= f'Subject : Monday Motivation\n\n {random_quote}')




