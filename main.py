import smtplib
import datetime as dt
import random

import pandas

my_email = "yukwokng@yahoo.com"
password = "lkgpczgtbyunkabs"

# Today -----
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# name,email,year,month,day
# Test,test@email.com,1961,12,21
# [Fill this in!]

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    # print(birthday_person)
    # print(birthday_person["name"])
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # print(file_path)
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="billynyk@qq.com",
                            msg=f"Subject:Happy birthday !"
                                f"\n\n"
                                f"{contents}")

        #

#     all_quotes = quote_file.readlines()
#     quote = random.choice(all_quotes)

# print(quote)

# my_email = "yukwokng@yahoo.com"
# password="vmpfjhflkzrtspzp"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="billynyk@gmail.com",
#                         msg=f"Subject:famous string\n\n{quote}")
#
