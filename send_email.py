import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("EMAILAPPUSERNAME")
    password = os.getenv("EMAILNEWSPASSWORD")
    receiver = username
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

