import pandas
import smtplib
import random
import datetime as dt

my_email = "" # Write your email here
my_password = "" # Write your password app generator here

birthdays = pandas.read_csv("birthdays.csv")
birthdays_list = birthdays.to_dict(orient="records")


for birthday in birthdays_list:
    now = dt.datetime.now()

    month = birthday["month"]
    day = birthday["day"]
    name = birthday["name"]

    day_now = now.day
    month_now = now.month

    random_letter_number = random.randint(1, 3)
    letter_open = f"letter_templates/letter_{random_letter_number}.txt"
    with open(letter_open) as file:
        letter_txt = file.read()
        new_letter = letter_txt.replace("[NAME]", name)

    if day_now == day and month_now == month:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Happy Birthday!\n\n{new_letter}")



