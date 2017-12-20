#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import requests
import logging
import json
import BaseService
import BalanceService
import Utils
import itertools
import time

class TradeService(BaseService.BaseService):
	POST_TRADE_ADD = 'trade_add'
	POST_TRADE_CANCEL = 'trade_cancel'

	def __init__(self):
		super(TradeService, self).__init__('Trade')
		try:
			f = open('keys.json', 'r')
			conf = json.load(f)
			self.public_key = conf['trade']['public_key'] 
			self.private_key = conf['trade']['private_key']
		except Exception as e:
			raise

	def post_trade_add(self, coin, amount, price, trade_type):
		nonce = Utils.generate_nonce()
		original_params = {'coin' : coin, 'amount' : amount, 'price' : price, 'type' : trade_type,
							 'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		url = self.restful_url + TradeService.POST_TRADE_ADD
		self.logger.info('post_trade_add: %s, %s' % (url, params))
		response = requests.post(url, data = params)
		return response.content if response else ''	

	def post_trade_cancel(self, coin, trade_id):
		nonce = Utils.generate_nonce()
		original_params = {'coin' : coin, 'id' : trade_id, 'nonce' : nonce, 'key' : self.public_key}
		params = Utils.reformat_params(original_params, self.private_key)
		url = self.restful_url + TradeService.POST_TRADE_CANCEL
		self.logger.info('post_trade_cancel: %s, %s' % (url, params))
		response = requests.post(url, data = params)
		return response.content if response else ''	

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	tradeService = TradeService()
	balanceService = BalanceService.BalanceService()
	#result = tradeService.post_trade_add('doge', 2000000.0, 0.0001, 'buy')
	#print result
	print balanceService.post_trade_list('doge', 1483200000, 'open')
	result = tradeService.post_trade_cancel('doge', 123)
	print result
	print balanceService.post_trade_list('doge', 1483200000, 'open')

