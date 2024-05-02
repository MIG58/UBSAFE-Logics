from twilio.base.exceptions import TwilioRestException
import time

# Local Imports
from email_notif.mail import send_mail
from message.sms_notif import sms_alert
from sshlock.blockSSH import *
from blockusb.blockusb import *
from system_backup_restore.sysBackupRestore import *
from tor_lock.torLock import *
from firewall_setup.firewall import *

# msg = "Mail System is working ," ; tmail = "abhiraj123sardar@gmail.com" ; p = "Abhiraj"
# msg = "Mail System is working ," ; tmail = "michaelg17801@gmail.com" ; p = "Michael"


def mailalert(pname, tmail, msg,):  # Outer Format PersonName,Target_Mail,Message
    # Inner Format Message, Target mail, Person_Name
    send_mail(msg, tmail, pname)


def smsalert(msg2, tphone):
    sms_alert(msg2, tphone)  # Message , Target Registered Phone


def lockssh(x):
    if (x):
        assh()  # Activate SSH MASK
    else:
        bssh()  # Deactivate SSH MASK


def usb_lock():
    busb()  # After block make sure to reboot to perform unblock
    # time.sleep(20) # 20 Sec
    ubusb()  # After unblock make sure to reboot and plugin device then press unblock button


def sysBackupRestore(x):
    if (x):
        sysbackup()
    else:
        sysrestore()


def firewall():
    fwall()


# --------------------------------------------WORKING LOGIC CODES---------------------------------------------

# SSH SYSTEM IS WORKING AS BASIC MASK & UNMASK
lockssh(1)

# MAIL-ALERT SYSTEM IS WORKING
# pname = "Michael" ; tmail = "michaelg17801@gmail.com" ; msg = "Mail System is working ," ;
mailalert(pname,tmail,msg,)

# SMS-ALERT SYSTEM IS WORKING
# tphone="+919163439756"; msg2="SMS system is working";
smsalert(msg2,tphone)

# USB Block is Working
usb_lock()

# System Backup & Restore Working
sysBackupRestore(1)

# Only Lock Tor (No Unblock) Working
tor_lock()

# Default Firewall setup Working
fwall()
