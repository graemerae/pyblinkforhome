# pyblinkforhome
Simple Python Library for accessing Blink For Home Cameras. http://blinkforhome.com

1) Make sure you have Python and a few common modules - argparse, json, requests, urllib, ConfigParser

2) Rename the blink.ini.sample file to blink.ini and put in your Blink Credentials.

3) Run as : python blink.py --action ACTION
   Where action can be arm,disarm,isArmed,Homescreen, clips, events.

TODO:
  Build a quick flask wrapper to allow login, format Homescreen, clips etc.
  Build a more robust hook into Homebridge.
  Add geofencing code.

 
NOTES:
  I am not affiliated with blinkforhome other than being a happy customer.  I wrote this code to hook Blink into my Homekit network to allow geofencing and other scenes to control arming and disarming of the cameras.
  
  Inspired by:
  
    http://robsblog.robgmartin.com/post/144557833493/integrating-blink-cameras-with-apple-homekit
    
    https://github.com/nfarina/homebridge
    
    
  

