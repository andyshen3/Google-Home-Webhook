import os
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('To call San Jose IT Services, press 1. To call Japan IT Services, press 2. To call Philippines IT Services, press 3.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)

def handleCall():
	client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

	call = client.calls.create(
		to=os.environ.get("MY_NUMBER"),
		from_=os.environ.get("TWILIO_NUMBER"),
		url="https://handler.twilio.com/twiml/EH169b198afd1064eeb01690ed4785c5e8",
		record = True)

	print(call.sid)
