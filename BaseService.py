#! /usr/bin/python
# -*- encoding: utf-8 -*-
# @Author: DZF

import sys
import json
import logging

class BaseService(object):
	def __init__(self, serviceType):
		self.type = serviceType
		self.logger = logging.getLogger('CoinEgg %s Logger' % serviceType)
		self.logger.setLevel(logging.DEBUG)
		try:
			f = open('conf.json', 'r')
			conf = json.load(f)
			self.base_url = conf['base_url'] 
			self.api_url = conf['api_url']
			self.restful_url = self.base_url + self.api_url
		except Exception as e:
			raise