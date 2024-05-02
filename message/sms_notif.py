import twilio
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from message import keys


def sms_alert(msg, target_phone):
    try:
        target_phone
        target_msg = msg
        client = Client(keys.account_sid, keys.auth_token)

        message = client.messages.create(
            body=target_msg,
            from_=keys.twilio_number,  # your custom phone number
            to=target_phone  # the recipient's phone number
        )
    # print(message.sid)  # To show message ID
    except TwilioRestException as e:
        print("Trial Account! Number is not registered "+target_phone)
