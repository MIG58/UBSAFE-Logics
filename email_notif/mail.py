import ssl
import smtplib
# from cred import *
from email.message import EmailMessage

global sender_mail, passwd, reciever_mail, subject, body

sender_mail = 'sourcex5688@gmail.com'
spasswd = 'mppojwlhcnibemhi'

# reciever_mail = 'ksuman2004.sr@gmail.com'
# reciever_mail = 'abhiraj123sardar@gmail.com'
reciever_mail = 'michaelg17801@gmail.com'

# target_email = 'pantherb201@gmail.com'

subject = 'Alert from UBSAFE'

# body = 'The System might be inturrepted / shutdown'
# t_mail - Target mail
# App PASS SourceX - mppojwlhcnibemhi

def send_mail(msg, t_mail, name):
    body = "Hello, "+name+" "+msg
    reciever_mail = t_mail
    em = EmailMessage()
    em['From'] = sender_mail
    em['To'] = t_mail
    em['Subject'] = subject
    em.set_content(body)
    # print(reciever_mail)    # To know that correct mail in comming or not
    # print(t_mail)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_mail, spasswd)
        smtp.sendmail(sender_mail, reciever_mail, em.as_string())


# send_mail("ksuman2004.sr@gmail.com")
# send_mail("ABCD", "michaelg17801@gmail.com", "MIG")

# # connect to the SMTP server
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
# smtp_connection.ehlo()
# smtp_connection.starttls()
# smtp_connection.login(email_address, email_password)