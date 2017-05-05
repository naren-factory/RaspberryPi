#!/usr/bin/python2.7

import string  ## required to join together 'from', 'to', 'subject', etc. to a string
from smtplib import SMTPException
from smtplib import SMTP_SSL as SMTP  ## Import secure smtp-library to provide email functions

import garage_watchdog_config as config


def send_mail(self, subject):
    # define sender email account
    smtp_email_addr = config.SENDER_EMAIL_ADDRESS
    smtp_server = config.SMTP_SERVER
    smtp_port = config.SMTP_PORT  # depending on provider and security level
    smtp_user = config.SMTP_USERNAME
    smtp_pass = config.SMTP_PASSWORD
    SUBJECT = subject
    FROM = smtp_email_addr
    TEXT = subject
    # send reminder email
    TO = config.KEEP_ALIVE_MSG_SENT_TO
    BODY = string.join(("FROM: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "", TEXT), "\r\n")
    try:
        smtpObj = SMTP(smtp_server, smtp_port)
        smtpObj.set_debuglevel(0)
        smtpObj.login(smtp_user, smtp_pass)
        smtpObj.sendmail(FROM, TO, BODY)
        print ('Successfully sent keep alive email to', TO)
        smtpObj.quit()
    except SMTPException, e:
        print "Error: unable to send email to ", TO
        print e