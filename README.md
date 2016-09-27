# pyblinkforhome
Simple Python Library for accessing BlinkForHome Cameras.


1) Install Python and a few common modules - argparse, json, requests, urllib, ConfigParser

2) Copy the blink.ini.sample file to blink.ini and put in your Bink Credentials.

3) Run as : python blink.py --action ACTION
   Where action can be arm,disarm,isArmed,Homescreen, clips, events.

TODO:
  Build a quick flask wrapper to allow login, format Homescreen, clips etc.
  Build a more robust hook into Homebridge.
  
 
 
NOTES:
  I am not affiliated with blinkforhome other than being a happy customer.  I wrote this code to hook Blink into my Homekit network to allow geofencing and other scenes to control arming and disarming of the cameras.
  
  Inspired by:
  
    http://robsblog.robgmartin.com/post/144557833493/integrating-blink-cameras-with-apple-homekit
    
    https://github.com/nfarina/homebridge
    
    
  

