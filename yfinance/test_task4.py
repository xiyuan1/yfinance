#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yfinance as yf
import unittest
import utils



symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]
  #check if self._calendar.index is being set properly by camel2title()
class TestEvent4(unittest.TestCase):
	def __init__(self, _calendar):
		self._calendar= _calendar

	def test_event_contains(self):
		self._calendar = None
		return True

	def test_event4(self):
		a = ['foo', 'bar', 'cad']
		self._calendar.index = utils.camel2title(a)
		print(self._calendar.index)
		print("hello word")
  
if __name__ == '__main__':
	unittest.main()