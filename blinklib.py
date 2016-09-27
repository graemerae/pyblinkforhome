import json, requests
import urllib


def getToken(em,pw):
	url='https://prod.immedia-semi.com/login'
	payload = {'password': pw, 'client_specifier': "iPhone 9.2 | 2.2 | 222", 'email': em}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	at= data['authtoken']['authtoken']
	return at

def getNetworks(em,pw):
	url='https://prod.immedia-semi.com/login'
	payload = {'password': pw, 'client_specifier': "iPhone 9.2 | 2.2 | 222", 'email': em}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	networks=data['networks']
	return networks.keys()

def getHomescreen(at):
	url='https://prod.immedia-semi.com/homescreen'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data


def getEvents(at,nt):
	url='https://prod.immedia-semi.com/events/network/'+nt
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data


def getClips(at,nt):
	url='https://prod.immedia-semi.com/events/network/'+nt
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	#loop through and only keep type:Motion
	events=data['event']
	motion=[]
	for i in xrange(len(events)):
		if (events[i]["type"] == "motion" and "video_url" in events[i]):
			motion.append(events[i])
	return motion



def arm(at,nt):
	url='https://prod.immedia-semi.com/network/'+nt+'/arm'
	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def disarm(at,nt):
	url='https://prod.immedia-semi.com/network/'+nt+'/disarm'
	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def isArmed(at):
	url='https://prod.immedia-semi.com/homescreen'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data['network']['armed']

