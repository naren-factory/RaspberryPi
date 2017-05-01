#!/usr/bin/python2.7

##############################################################################
# Global settings
##############################################################################

# Describes all the garage doors being monitored
GARAGE_DOORS = [
    {
        'pin': 15,
        'name': "Main Garage Door",
        'alerts': [
            {
                'state': 'open',
                'time': 30,
                'recipients': [ 'sms:+19083136204', 'call:+19083136204' ]
            }
        ]
    }
]

# All messages will be logged to stdout and this file
LOG_FILENAME = "/var/log/pi_garage_alert.log"

##############################################################################
# Twilio settings
##############################################################################

TWILIO_ACCOUNT = 'ACc890573fc4f18e9d0b148da9e82215f1'
TWILIO_TOKEN = 'ca1be8a0f344e7c4eb13860a1eb1c9f4'

# SMS will be sent from this phone number
TWILIO_PHONE_NUMBER = '+19082666141'
