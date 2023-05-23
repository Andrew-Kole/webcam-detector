from dotenv import load_dotenv
import typing
import os
import smtplib
import imghdr
from email.message import EmailMessage

load_dotenv()
MAIL_PASSWORD: typing.Final = os.getenv("MAIL_PASSWORD")
MAIL_USER: typing.Final = os.getenv("MAIL_USER")
MAIL_RECEIVER: typing.Final = os.getenv("MAIL_RECEIVER")


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(MAIL_USER, MAIL_PASSWORD)
    gmail.sendmail(MAIL_USER, MAIL_RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == ("__main__"):
    send_email(image_path="images/13.png")