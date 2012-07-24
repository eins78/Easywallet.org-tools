#!/usr/bin/python

import os
import os.path
import urllib
import json
import socket
import re
import select
import sys
import codecs
import commands
import urllib2
import random
import pickle
from time import sleep
import datetime
import math
from decimal import Decimal
import subprocess
import argparse

SITE_URL="https://easywallet.org"
#SITE_URL="http://localhost:8000"

API_URL = SITE_URL+'/api/v1/'
LINE_DELIMITER = '\r\n'

parser = argparse.ArgumentParser(description='Generate coupons using easywallet.org')
parser.add_argument('wallet', action='store', help="easywallet.org wallet secret key")
parser.add_argument('-a', dest='amount', type=Decimal, default=Decimal(1), help='Amount')
parser.add_argument('--currency', dest='currency', default="USD", help='Currency')
parser.add_argument('-c', dest='count', type=int, default="5", help='How many coupons to generate')

args = parser.parse_args()
# print args

def call_api(url_suffix, data = None):
    f = urllib.urlopen(API_URL + url_suffix, data)
    data = f.read()
    # print data
    return json.loads(data)

def initiate_coupon(amount, currency, wallet_id):
    post_data = urllib.urlencode({'address': 'coupon', 'amount': amount, 'currency': currency})
    result = call_api('w/%s/payment' % wallet_id, post_data)
    return result

def format_btc_amount(amount):
    s = "%.8f" % (float(amount))
    return re.sub("\.?0+$", "", s)

def get_json(url, data={}):
    try:
        if data:
            f = urllib2.urlopen(
                url, data=data)
        else:
            f = urllib2.urlopen(
                url)
        result=f.read()
        final_json=json.loads(result)
        return final_json
    except Exception as inst:
        print "Unexpected error:", inst
        time.sleep(bs_seconds)
        return None


if __name__ == '__main__':

    wallet_id = args.wallet

    # output info
    print "Using "+SITE_URL+"/w/%s" % wallet_id

    balance_array = call_api('w/%s/balance_unconfirmed' % wallet_id)
    print "Balance: "+str(balance_array)

    for i in range(0, args.count):
        r = initiate_coupon(args.amount, args.currency, wallet_id)
        if r['successful']:
            print '"'+r['coupon']+'","'+str(args.amount)+'","'+str(args.currency)+'","'+str(datetime.datetime.now())+'"'
        else:
            print "Error:", r['message']
            exit(0)
    
   