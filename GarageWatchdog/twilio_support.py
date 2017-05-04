#!/usr/bin/python2.7
"""
support for sending SMS and making phone call using Twilio services
"""
import sys

from twilio.rest import Client

import garage_watchdog_config as config
from smtp_support import send_mail


def send_sms(self, recipient, msg):
    """Sends SMS message to specified phone number using Twilio.

    Args:
        recipient: Phone number to send SMS to.
        msg: Message to send. Long messages will automatically be truncated.
    """

    # User may not have configured twilio - don't initialize it until it's
    # first used
    if self.twilio_client is None:
        self.logger.info("Initializing Twilio")

        if config.TWILIO_ACCOUNT == '' or config.TWILIO_TOKEN == '':
            self.logger.error("Twilio account or token not specified - unable to send SMS!")
        else:
            self.twilio_client = Client(config.TWILIO_ACCOUNT, config.TWILIO_TOKEN)

    if self.twilio_client != None:
        self.logger.info("Sending SMS to %s: %s", recipient, msg)
        try:
            self.twilio_client.messages.create(
                to=recipient,
                from_=config.TWILIO_PHONE_NUMBER,
                body=truncate(msg, 140))
        except:
            self.logger.error("Exception sending SMS: %s", sys.exc_info()[0])
            reminder_text = "Exception sending SMS!!! Garage Door Open"
            send_mail(reminder_text)


def call_phone(self, recipient):
    """Make a call to specified phone number using Twilio.

    Args:
        recipient: Phone number to call.
    """

    # User may not have configured twilio - don't initialize it until it's
    # first used
    if self.twilio_client is None:
        self.logger.info("Initializing Twilio")

        if config.TWILIO_ACCOUNT == '' or config.TWILIO_TOKEN == '':
            self.logger.error("Twilio account or token not specified - unable to make a call!")
        else:
            self.twilio_client = Client(config.TWILIO_ACCOUNT, config.TWILIO_TOKEN)

    if self.twilio_client != None:
        self.logger.info("Calling.. %s:", recipient)
        try:
            self.twilio_client.calls.create(to=recipient,
                                            from_=config.TWILIO_PHONE_NUMBER,
                                            url="http://demo.twilio.com/docs/voice.xml")
        except:
            self.logger.error("Exception Calling: %s", sys.exc_info()[0])
            reminder_text = "Exception Calling!! Garage Door Open"
            send_mail(reminder_text)


def truncate(input_str, length):
    """Truncate string to specified length

    Args:
        input_str: String to truncate
        length: Maximum length of output string
    """
    if len(input_str) < (length - 3):
        return input_str

    return input_str[:(length - 3)] + '...'