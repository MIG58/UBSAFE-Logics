from twilio.base.exceptions import TwilioRestException

# Local Imports
from email_notif.mail import send_mail
from message.sms_notif import sms_alert
from sshlock.blockSSH import *

# reciever_mail = 'ksuman2004.sr@gmail.com'
# reciever_mail = 'abhiraj123sardar@gmail.com'

# msg = "Mail System is working ," ; tmail = "abhiraj123sardar@gmail.com" ; p = "Abhiraj Deshapriya Fuckboy" 
# msg = "Mail System is working ," ; tmail = "ksuman2004.sr@gmail.com" ; p = "Suman Howrah Fuckboy" 
# msg = "Mail System is working ," ; tmail = "michaelg17801@gmail.com" ; p = "Michael" 

def mailalert(pname,tmail,msg,): # Outer Format PersonName,Target_Mail,Message
     
    send_mail(msg,tmail,pname) # Inner Format Message, Target mail, Person_Name

# tphone1="+919330668959"
# tphone2="+918697499539"
# tphone="+91916349756"
# msg2="SMS system is working"; 

def smsalert(msg2,tphone):
    sms_alert(msg2,tphone) # Message , Target Registered Phone


def lockssh():
    bssh()


# assh()
# lockssh()

# alias sS='sudo systemctl status ssh'




