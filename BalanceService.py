#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import requests
import logging
import json
import BaseService
import Utils
from urllib import urlencode

class BalanceService(BaseService.BaseService):
	POST_BALANCE = 'balance'
	POST_TRADE_LIST = 'trade_list'
	POST_TRADE_VIEW = 'trade_view'

	def __init__(self):
		super(BalanceService, self).__init__('Balance')
		try:
			f = open('keys.json', 'r')
			conf = json.load(f)
			self.public_key = conf['query']['public_key'] 
			self.private_key = conf['query']['private_key']
		except Exception as e:
			raise

	def post_balance(self):
		nonce = Utils.generate_nonce()
		original_params = {'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		url = self.restful_url + BalanceService.POST_BALANCE
		self.logger.info('post_balance: %s, %s' % (url, params))
		response = requests.post(url, data = params)
		return response.content if response else ''			

	def post_trade_list(self, coin, since = 0, trade_type = 'all'):
		nonce = Utils.generate_nonce()
		original_params = {'coin' : coin, 'since' : since, 'type' : trade_type, 'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		url = self.restful_url + BalanceService.POST_TRADE_LIST
		self.logger.info('post_trade_list: %s, %s' % (url, params))
		response = requests.post(url, data = params)
		return response.content if response else ''	

	def post_trade_view(self, coin, trade_id):
		nonce = Utils.generate_nonce()
		original_params = {'coin' : coin, 'id' : trade_id, 'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		url = self.restful_url + BalanceService.POST_TRADE_VIEW
		self.logger.info('post_trade_view: %s, %s' % (url, params))
		response = requests.post(url, data = params)
		return response.content if response else ''		

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	balanceService = BalanceService()
	# balance = balanceService.post_balance()
	# print balance
	trade_list = balanceService.post_trade_list('doge', 0, 'open')
	print trade_list
	trade_view = balanceService.post_trade_view('doge', 6860502)
	print trade_view	