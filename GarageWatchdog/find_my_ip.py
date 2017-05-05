#!/usr/bin/python2.7
"""
It finds the external IP for the caller
"""

import urllib2

def get_my_ip():
    try:
        ext_ip = urllib2.urlopen('https://ifcfg.me/ip').read()
        return ext_ip
    except:
        return ""