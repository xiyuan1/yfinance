#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import yfinance as yf
import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pandas as pd
import util



symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]
  #check if self._calendar.index is being set properly by camel2title()
class TestEvent4(unittest.TestCase):
    def __init__(self):
        self.msft = yf.Ticker("MSFT")
        self.utils_mock = patch('yfinance.base.utils.get_json', autospec=True).start()
        self.addCleanup(patch.stopall)

	def test_fill_contains(self):
		a = ['earning', 'revenue', 'avg']
		self.calendar.index = util.camel2title(a)
		check = self.calendar.index
		print(check)
		self.assert(check, util.camel2title(a))



	if __name__ == '__main__':
		unittest.main()
  
  