
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

# print(quote)

my_email = "yukwokng@yahoo.com"
password="vmpfjhflkzrtspzp"

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="billynyk@gmail.com",
                        msg=f"Subject:famous string\n\n{quote}")










# import smtplib
#
# my_email = "yukwokng@yahoo.com"
# password="vmpfjhflkzrtspzp"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="billynyk@gmail.com",
#                         msg="Subject:testing\n\nThis is the second try"
#                             "content body.")
#
#
# # import datetime as dt
# #
# now = dt.datetime.now()
# print(now)



