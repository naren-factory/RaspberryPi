#!/usr/bin/python2.7

##############################################################################
# Global settings
##############################################################################

# Describes all the garage doors being monitored
GARAGE_DOORS = [
#    {
#        'pin': 16,
#        'name': "Garage Door 1",
#        'alerts': [
#            {
#                'state': 'open',
#                'time': 120,
#                'recipients': [ 'sms:+11112223333', 'sms:+14445556666' ]
#            },
#            {
#                'state': 'open',
#                'time': 600,
#                'recipients': [ 'sms:+11112223333', 'sms:+14445556666' ]
#            }
#        ]
#    },

    {
        'pin': 15,
        'name': "Example Garage Door",
        'alerts': [
#            {
#                'state': 'open',
#                'time': 120,
#                'recipients': [ 'sms:+11112223333', 'email:someone@example.com', 'twitter_dm:twitter_user', 'pushbullet:access_token', 'gcm', 'tweet', 'ifttt:garage_door' ]
#            },
#            {
#                'state': 'open',
#                'time': 600,
#                'recipients': [ 'sms:+11112223333', 'email:someone@example.com', 'twitter_dm:twitter_user', 'pushbullet:access_token', 'gcm', 'tweet', 'ifttt:garage_door' ]
#            }
        ]
    }
]

# All messages will be logged to stdout and this file
LOG_FILENAME = "/var/log/pi_garage_alert.log"

##############################################################################
# Email settings
##############################################################################

SMTP_SERVER = 'localhost'
SMTP_PORT = 25
SMTP_USER = ''
SMTP_PASS = ''
EMAIL_FROM = 'Garage Door <user@example.com>'
EMAIL_PRIORITY = '1'
# 1 High, 3 Normal, 5 Low

##############################################################################
# Twilio settings
##############################################################################

TWILIO_ACCOUNT = 'ACc890573fc4f18e9d0b148da9e82215f1'
TWILIO_TOKEN = 'ca1be8a0f344e7c4eb13860a1eb1c9f4'

# SMS will be sent from this phone number
TWILIO_PHONE_NUMBER = '+19082666141'

##############################################################################
# Google Cloud Messaging settings
##############################################################################

GCM_KEY = ''
GCM_TOPIC = ''

##############################################################################
# IFTTT Maker Channel settings
# Create an applet using the "Maker" channel, pick a event name,
# and use the event name as a recipient of one of the alerts,
# e.g. 'recipients': [ 'ifft:garage_event' ]
#
# Get the key by going to https://ifttt.com/services/maker/settings.
# The key is the part of the URL after https://maker.ifttt.com/use/.
# Do not include https://maker.ifttt.com/use/ in IFTTT_KEY.
##############################################################################

IFTTT_KEY = ''
