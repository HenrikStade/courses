
import datetime as dt
import random
import smtplib

my_email = "springtiden@gmail.com"
my_password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nipptiden@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email.")

now = dt.datetime.now()
year = now.year
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1987, month=9, day=13)


with open("quotes.txt", "r") as f:
    quotes_list = f.readlines()

if day_of_week == 1:
    quote = random.choice(quotes_list)


