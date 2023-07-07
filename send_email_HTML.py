import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def send_email_html(subject, message=""):
    host = "smtp.gmail.com"
    port = 465
    sender_username = "bryan.patrick.a.murphy@gmail.com"
    password = os.getenv("WebPortfolio_Password")

    recipient = "bryan.patrick.a.murphy@gmail.com"

    context = ssl.create_default_context()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_username
    msg["To"] = recipient

    html = MIMEText(message, "html")

    msg.attach(html)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_username, password)
        server.sendmail(sender_username, recipient, msg.as_string())

# test1 = """
# <b>Hello.</b><br><br>
# <font size="4">My name is David.</font><br><br>
# <u>Bye!</u>
# """
#
# test2 = """
# <html>
#   <head>
#     <style>
#       body {
#         font-family: "Minion Pro", serif;
#         font-size: 12pt;
#       }
#     </style>
#   </head>
#   <body>
#     <b>Hello.</b><br><br>
#     My name is David.<br><br>
#     <u>Bye!</u><br><br>
#     Content2
#   </body>
# </html>
# """
#
# samplesentence = "Never ever Have I ever: HAD a RINGO that was a GOOD BOY!!!"
#
# test3 = f"""<p style="font-family: Minion Pro; font-size: 14pt;">
#     <b>Hello.</b><br><br>
#     My name is David.<br><br>
#     <u>Bye!</u><br><br>
#     Content3<br>
#     {samplesentence}</p>
#     """

# send_email_html(content3)

# Minion Pro is still the best, stay winning.