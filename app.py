#!/usr/bin/env python

import urllib
import json
import os
import call
import send_sms

from flask import Flask
from flask import request
from flask import make_response
from call import handleCall
from send_sms import handleMessage


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

#Returns the PSID values stored for each person
def handleFindPSID(req):
	result = req.get("result")
	parameters = result.get("parameters")
	name = str.lower(parameters.get("user-name"))

	psid = {'name': "value"}

	if name in psid:
		speech = name + ", your PSID is " + str(psid[name]) + "."
	else:
		speech = "Sorry, that user is not in our system."

	print("Response:")
	print(speech)

	return {
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-findpsid"
	}

#Returns the cost center values stored for each person
def handleFindCostCenter(req):
	result = req.get("result")
	parameters = result.get("parameters")
	name = str.lower(parameters.get("user-name"))

	costCenter = {'name': "value"}

	if name in costCenter:
		speech = name + ", your cost center is " + str(costCenter[name]) + "."
	else:
		speech = "Sorry, that user is not in our system."

	print("Response:")
	print(speech)

	return{
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-findCostCenter"
	}

#Returns the onboard date values stored for each person
def handleFindOnboardDate(req):
	result = req.get("result")
	parameters = result.get("parameters")
	name = str.lower(parameters.get("user-name"))

	onBoardDate = {'name': "value"}

	if name in onBoardDate:
		speech = name + ", your onboard date is " + str(onBoardDate[name]) + "."
	else:
		speech = "Sorry, that user is not in our system."

	print("Response:")
	print(speech)

	return{
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-findOnboardDate"
	}

#Returns the full name of a requested acronym
def handleGetAcronym(req):
	result = req.get("result")
	parameters = result.get("parameters")
	word = str.upper(parameters.get("acronyms"))

	acronym = {'name': "value"}

	if word in acronym:
		speech = acronym[word] + "."
	else:
		speech = "Sorry, I could not find anything about that acronym."

	print("Response:")
	print(speech)

	return{
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-getAcronym"
	}

#Returns the manager of the employee the user inputs
def handleFindManager(req):
	result = req.get("result")
	parameters = result.get("parameters")
	user = str.lower(parameters.get("user-name"))

	manager = {'name': "value"}

	if user in manager:
		speech = user + "'s manager is " + manager[user] + "."
	else:
		speech = "Sorry, that user is not in our system."

	print("Response:")
	print(speech)

	return {
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-findManager"
	}

#Extract the parameters provided by the user, store the data.
def getCaseParameters(req):
	result = req.get("result")
	parameters = result.get("parameters")
	
	user = str.lower(parameters.get("user-name"))
	case = parameters.get("case")
	category = "none specified"

	if(parameters.get("employee-service") != ""):
		category = "employee-service"
	elif(parameters.get("infrastructure") != ""):
		category = "infrastructure"
	elif(parameters.get("systems-applications") != ""):
		category = "systems-applications"

	data = [user, case, category]

	return data


def makeWebhookResult(req):
    if req.get("result").get("action") == "find.psid":
        return handleFindPSID(req)

    elif req.get("result").get("action") == "find.costCenter":
    	return handleFindCostCenter(req)

    elif req.get("result").get("action") == "find.onboardDate":
    	return handleFindOnboardDate(req)

    elif req.get("result").get("action") == "get.acronym":
    	return handleGetAcronym(req)

    elif req.get("result").get("action") == "find.manager":
    	return handleFindManager(req)

    elif req.get("result").get("action") == "file.case":
    	data = getCaseParameters(req)
    	return handleMessage(data)

    elif req.get("result").get("action") == "DefaultFallbackIntent.DefaultFallbackIntent-yes":
    	return handleCall()

    else:
    	return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
