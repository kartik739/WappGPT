import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
  '''
    Send message to a Telegram user.
    Parameters:
        - to(str): sender whatsapp number in this whatsapp:+917895230590 form
        - message(str): text message to send
    Returns:
        - None
    '''

  _ = client.messages.create(from_='whatsapp:+14155238886',
                             body=message,
                             to=to)
