import smtplib
# metadata about images
import imghdr
from email.message import EmailMessage

PASSWORD = ""
SENDER = "indulahari6@gmail.com"
RECEIVER = "indulahari6@gmail.com"


def send_mail(image_path):
    mail_message = EmailMessage()
    mail_message["Subject"] = "New customer showed up!"
    mail_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb")as file:
        content = file.read()
    mail_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, mail_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_mail(image_path="images/19.png")