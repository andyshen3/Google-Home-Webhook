import os
from twilio import twiml
from twilio.rest import Client

def handleCall():
	print(TWILIO_ACCOUNT_SID)
	print(TWILIO_AUTH_TOKEN)
	print(MY_NUMBER)
	print(TWILIO_NUMBER)
	client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

	call = client.calls.create(
		to=MY_NUMBER,
		from_=TWILIO_NUMBER,
		url="http://demo.twilio.com/docs/voice.xml")

	print(call.sid)

handleCall()
