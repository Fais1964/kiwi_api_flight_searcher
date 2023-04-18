from twilio.rest import Client
import os

class NotificationManager:

    def send_mail(self, body):

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_ACCOUNT_AUTH_TOKEN")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_=f'whatsapp:{os.getenv("TWILIO_BOT_NR")}',
        body=f'Hey, Sky-Search Update: {body}',
        to=f'whatsapp:{os.getenv("MY_PHONE_NR")}'
        )



