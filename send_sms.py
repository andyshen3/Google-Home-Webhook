import os
from twilio import twiml
from twilio.rest import Client

def handleMessage():
	client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

	message = client.messages.create(
		to=os.environ.get("MY_NUMBER"),
		from_=os.environ.get("TWILIO_NUMBER"),
		body="Hello from Python!")

	print(message.sid)
