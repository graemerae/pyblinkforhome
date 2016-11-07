import json, requests
import urllib
import os


def getToken(em,pw):
	url='https://prod.immedia-semi.com/login'
	payload = {'password': pw, 'client_specifier': "iPhone 9.2 | 2.2 | 222", 'email': em}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	at= data['authtoken']['authtoken']
	return at


def getNetworks(em,pw):
	url='https://rest.prod.immedia-semi.com/login'
	payload = {'password': pw, 'client_specifier': "iPhone 9.2 | 2.2 | 222", 'email': em}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	networks=data['networks']
	return networks.keys()

def getHomescreen(at):
	url='https://rest.prod.immedia-semi.com/homescreen'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data


def listCameras(at,nt):
	url='https://rest.prod.immedia-semi.com/homescreen'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	#loop through and only return deviceIDs and Name
	devices=data['devices']
	deviceList=[]
	for i in xrange(len(devices)): 
		if devices[i]["device_type"] == "camera":
			deviceList.append([devices[i]['name'],devices[i]['device_id']])
	return deviceList
 
def getEvents(at,nt):
	url='https://rest.prod.immedia-semi.com/events/network/'+nt
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data


def listClips(at,nt):
	url='https://rest.prod.immedia-semi.com/events/network/'+nt
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

def getClip(at,clipURL):
	url='https://rest.prod.immedia-semi.com'+clipURL
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	with open(os.path.basename(clipURL), 'wb') as fd:
  		fd.write(r.content)


def liveCameras(at,nt,id):
	#url='https://prod.immedia-semi.com/api/v2/network/'+nt+'/camera/'
	url='https://rest.prod.immedia-semi.com/api/v2/network/'+nt+'/camera/'+id+'/liveview'

	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def makeStill(at,nt,id):
	url='https://rest.prod.immedia-semi.com/network/'+nt+'/camera/'+id+'/thumbnail'
	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def getStill(at,nt,id):
	#There needs to be a delay - wait for the command to finish from makeStill via polling.
	url='https://prod.immedia-semi.com/network/'+nt+'/camera/'+id+'/'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
 	getClip(at,data['camera_status']['thumbnail']+'.jpg')
	return data['camera_status']['thumbnail']



def arm(at,nt):
	url='https://rest.prod.immedia-semi.com/network/'+nt+'/arm'
	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def disarm(at,nt):
	url='https://rest.prod.immedia-semi.com/network/'+nt+'/disarm'
	payload = {}
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.post(url, data = json.dumps(payload), headers = headers)
	data = json.loads(r.text)
	return data

def isArmed(at):
	url='https://rest.prod.immedia-semi.com/homescreen'
	headers = {'Host': 'prod.immedia-semi.com', 'TOKEN_AUTH': at}
	r = requests.get(url, headers = headers)
	data = json.loads(r.text)
	return data['network']['armed']

