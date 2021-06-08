import smtplib

my_email = "yukwokng@yahoo.com"
password="vmpfjhflkzrtspzp"

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="billynyk@gmail.com",
                        msg="Subject:testing\n\nThis is the content body.")


