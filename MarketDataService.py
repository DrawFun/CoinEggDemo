#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import BaseService
import requests
import logging

class MarketDataService(BaseService.BaseService):
	GET_TICKER = 'ticker'
	GET_ALL_TICKERS = 'allticker'
	GET_DEPTH = 'depth'
	GET_ORDERS = 'orders'

	def __init__(self):
		super(MarketDataService, self).__init__('MarketData')

	def get_ticker(self, coin):
		param = {'coin' : coin}
		url = self.restful_url + MarketDataService.GET_TICKER
		self.logger.info('get_ticker: %s, %s' % (url, param))
		response = requests.get(url, params = param)
		return response.content if response else ''

	def get_all_tickers(self):
		url = self.restful_url + MarketDataService.GET_ALL_TICKERS
		self.logger.info('get_all_tickers: %s' % url)
		response = requests.get(url)
		return response.content if response else ''		

	def get_depth(self, coin):
		param = {'coin' : coin}
		url = self.restful_url + MarketDataService.GET_DEPTH
		self.logger.info('get_depth: %s, %s' % (url, param))
		response = requests.get(url, params = param)
		return response.content if response else ''

	def get_orders(self, coin):
		param = {'coin' : coin}
		url = self.restful_url + MarketDataService.GET_ORDERS
		self.logger.info('get_orders: %s, %s' % (url, param))
		response = requests.get(url, params = param)
		return response.content if response else ''		


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	marketDataService = MarketDataService()
	ticker_response = marketDataService.get_ticker('btc')
	print ticker_response
	assert(len(ticker_response))
	all_tickers_response = marketDataService.get_all_tickers()
	print all_tickers_response
	assert(len(all_tickers_response))
	depth_response = marketDataService.get_depth('btc')
	print depth_response
	assert(len(depth_response))
	orders_response = marketDataService.get_orders('btc')
	print orders_response
	assert(len(orders_response))
