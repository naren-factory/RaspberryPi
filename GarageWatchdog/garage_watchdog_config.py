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
                'recipients': [ 'sms:+1ABCDEFGHIJ', 'call:+1ABCDEFGHIJ' ]
            }
        ]
    }
]

# All messages will be logged to stdout and this file
LOG_FILENAME = "/var/log/pi_garage_alert.log"

##############################################################################
# Twilio settings
##############################################################################

TWILIO_ACCOUNT = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_TOKEN = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

# SMS will be sent from this phone number
TWILIO_PHONE_NUMBER = '+1ABCXYZERTY'

##############################################################################
# SMTP settings
##############################################################################
SENDER_EMAIL_ADDRESS = 'xxxx@domain.com'
SMTP_SERVER = 'xxxxxxx'
SMTP_PORT = 123
SMTP_USERNAME = 'username@domail.com'
SMTP_PASSWORD = 'password'

##############################################################################
# Keep alive message settings
##############################################################################

KEEP_ALIVE_MSG_DURATION = 604800 # one week in seconds
KEEP_ALIVE_MSG_SENT_TO = 'sendto@domain.com' # send the keep alive msg to this email address 