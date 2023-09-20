from twilio.base.exceptions import TwilioRestException

# Local Imports
from email_notif.mail import send_mail
from message.sms_notif import sms_alert

# reciever_mail = 'ksuman2004.sr@gmail.com'
# reciever_mail = 'abhiraj123sardar@gmail.com'

# msg = "Mail System is working ," ; tmail = "abhiraj123sardar@gmail.com" ; p = "Abhiraj Deshapriya Fuckboy" 
# msg = "Mail System is working ," ; tmail = "ksuman2004.sr@gmail.com" ; p = "Suman Howrah Fuckboy" 
msg = "Mail System is working ," ; tmail = "michaelg17801@gmail.com" ; p = "Michael" 
send_mail(msg,tmail,p) # Message, Target mail, Person_Name

# tphone1="+919330668959"
# tphone2="+918697499539"
tphone="+91916349756"
msg2="SMS system is working"; 
sms_alert(msg2,tphone) # Message , Target Registered Phone




