import os
from twilio import twiml
from twilio.rest import Client

def handleCall():
	client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

	call = client.calls.create(
		to=os.environ.get("MY_NUMBER"),
		from_=os.environ.get("TWILIO_NUMBER"),
		url="http://demo.twilio.com/docs/voice.xml")

	print(call.sid)

handleCall()
