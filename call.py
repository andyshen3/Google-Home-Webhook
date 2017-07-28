import os
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather

def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('To call San Jose IT Services, press 1. To call Japan IT Services, press 2. \
    			To call Philippines IT Services, press 3.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)

def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            return handleCall()
        elif choice == '2':
            resp.say('You need support. We will help!')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
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
