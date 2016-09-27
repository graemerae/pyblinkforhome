import argparse
import json, requests
import urllib
import blinklib as bl
import ConfigParser

#Get the Action
parser = argparse.ArgumentParser(description='Pass Parameters')
parser.add_argument(  '--action', nargs='?',  required=True, help='Action arm|disarm|homescreen|events|isarmed|clips'  )
parser.add_argument(  '--debug', nargs='?', type=int, default=0, required=False, help='Debug Level Output'  )
a = parser.parse_args()


#Read IN USER/PASS FROM A CONFIG FILE blink.ini
#
#File Format:
#[BlinkAuth]
#Username: Your_blink_username/emailaddress
#Password: Your_blink_password
#

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:    
        dict1[option] = Config.get(section, option)
    return dict1
Config = ConfigParser.ConfigParser()
Config.read("blink.ini")

#Set Username/Pass
username = ConfigSectionMap("BlinkAuth")["username"]
password = ConfigSectionMap("BlinkAuth")["password"]

#Get Authtoken based on login/password
authtoken=bl.getToken(username,password)
#Get List of Networks (assuming only one for now)
networks=bl.getNetworks(username,password)

if a.debug >0: 
	print "Auth Token"
	print authtoken
	print "First Network"
	print networks[0]

if a.action == "arm":
	print "Arming..."
	arm=bl.arm(authtoken,networks[0])
	if a.debug >0: print json.dumps(arm, indent=4, separators=(',', ': '))

elif a.action == "disarm":
	print "Disarming..."
	disarm=bl.disarm(authtoken,networks[0])
	if a.debug >0: print json.dumps(disarm, indent=4, separators=(',', ': '))

elif a.action == "status":
	print "STATUS"

elif a.action == "homescreen":
	print "Homescreen"
	homescreen=bl.getHomescreen(authtoken)
	print json.dumps(homescreen, indent=4, separators=(',', ': '))

elif a.action == "events":
	print "Events"
	events=bl.getEvents(authtoken,networks[0])
	print json.dumps(events, indent=4, separators=(',', ': '))

elif a.action == "clips":
	print "Clips"
	clips=bl.getClips(authtoken,networks[0])
	print json.dumps(clips, indent=4, separators=(',', ': '))

elif a.action == "isarmed":
	print bl.isArmed(authtoken)

else:
	print "Unknown Command"




