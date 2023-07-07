import smtplib
from email.message import EmailMessage
import os
import filetype
import time

password = os.getenv("WebPortfolio_Password")
sender = "bryan.patrick.a.murphy@gmail.com"
receiver = "bryan.patrick.a.murphy@gmail.com"
filename = time.strftime("%Y-%m-%d__%H-%M-%S")

def send_email(image_path):
    message = EmailMessage()
    message["Subject"] = "A wild Missingno has appeared!"
    message.set_content("See attached image for details!")

    with open(image_path, "rb") as imagefile:
        image_content = imagefile.read()
    message.add_attachment(image_content, maintype="image", subtype=filetype.guess(image_path).extension,
                           filename=f"{filename}")
    # why the None? See Notebook

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(r"static_images/test_image.jpg")
