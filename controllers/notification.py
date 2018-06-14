"""
notification.py
This is the reservation class file
"""
import datetime
import tester
from twilio.rest import Client


class Notification(object):
    def __init__(self):
        pass

    """a class that care about sending notification to customers."""
    def send_sms(self,mobile_number,sms_message):
        account_sid = tester.Tester.account_sid
        # Your Auth Token from twilio.com/console
        auth_token  = tester.Tester.auth_token
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=mobile_number,
            from_=tester.Tester.twilio_mobile, #enter your twilio number
            body=sms_message)
