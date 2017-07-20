import os
from twilio import twiml
from twilio.rest import Client

def handleMessage(data):
	client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

	content = "Case filed by: " + data[0] + "Case information:" + data[1] + "Category:" + data[2]
	message = client.messages.create(
		to=os.environ.get("MY_NUMBER"),
		from_=os.environ.get("TWILIO_NUMBER"),
		body=content)

	print(message.sid)
