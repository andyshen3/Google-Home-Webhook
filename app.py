#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
#from call.py import handleCall

#from twilio.rest import Client

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

	psid = {'andy shen': 27932, 'frank wang': 28592, 'vincent wang': 26371}

	speech = name + ", your PSID is " + str(psid[name]) + "."

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

	costCenter = {'andy shen': "AMT.1741G", 'frank wang': "AMT.1361G", \
	'vincent wang': "AMT.1816G"}

	speech = name + ", your cost center is " + str(costCenter[name]) + "."

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

	onBoardDate = {'andy shen': "June 7th, 2017", 'frank wang': \
	"February 18th, 2006", 'vincent wang': "August 28th, 2002"}

	speech = name + ", your onboard date is " + str(onBoardDate[name]) + "."

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

	acronym = {'APAC': "APAC stands for Asia Pacific", \
	'ACE': "ACE stands for Advanced Threat-Centric Education", \
	'ADC': "ADC stands for Access Document Control", \
	'APT': "APT stands for Advanced Persistent Threats", \
	'BP': "BP stands for Business Process", \
	'BU': "BU stands for Business Unit", \
	'CPM': "CPM stands for Trend Micro Core Protection Module", \
	'DSM': "DSM stands for Deep Security Manager", \
	'DD': "DD stands for Deep Discovery"}

	speech = acronym[word] + "."

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

	manager = {'andy shen': "felix jen", 'frank wang': "felix jen",\
	'vincent wang': "max cheng"}

	speech = user + "'s manager is " + manager[user] + "."

	print("Response:")
	print(speech)

	return {
	"speech": speech,
	"displayText": speech,
	#"data": {},
	#"contextOut": {[]},
	"source": "apiai-findManager"
	}

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

    #elif req.get("result").get("action") == "file.case":
    #	return handleCall()

    else:
    	return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
