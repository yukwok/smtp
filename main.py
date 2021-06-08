import smtplib

my_email = "yukwokng@yahoo.com"
password="abcde12345()"

connection = smtplib.SMTP("smtp.mail.yahoo.com")
print(f'connection: {connection}')
print( connection.starttls())
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="billynyk@gmail.com", msg="testing")
connection.close()


