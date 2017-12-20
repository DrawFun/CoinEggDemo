#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF
import hashlib
import hmac
import time
from collections import OrderedDict
from urllib import urlencode

#Nonce Length
JUBI_NONCE_LENGHT = 12

def getMd5Hash(s):
	m = hashlib.md5()
	m.update(s)
	return m.hexdigest()

def generate_nonce_from_timestamp():
	current_timestamp = time.time() * 1000
	return str(long(current_timestamp))

generate_nonce = generate_nonce_from_timestamp

def generate_signature(msg, private_key):
	msg = bytes(msg).encode('utf-8')
	k = bytes(getMd5Hash(private_key)).encode('utf-8')
	signature = hmac.new(k, msg, digestmod = hashlib.sha256).hexdigest()
	return signature

def reformat_params(params, private_key):
	orderDict = OrderedDict(params)
	param_str = urlencode(orderDict) #'&'.join(['%s=%s' % (str(k), str(v)) for (k, v) in orderDict.items()])
	signature = generate_signature(param_str, private_key)
	orderDict['signature'] = signature
	return orderDict

if __name__ == '__main__':
	pass


