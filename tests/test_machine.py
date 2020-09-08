import unittest
import os
from autotrading.machine.coinone_machine import CoinOneMachine
from autotrading.machine.bithumb_machine import BithumbMachine
import inspect

class TestData(unittest.TestCase):

    def setUp(self):
        self.coinone = CoinOneMachine()

    def test_coinone_get_ticker(self):
        print(inspect.stack()[0][3])
        result = self.coinone.get_ticker(currency_type="eth")
        assert result is not None
        print(result)

    def test_bithumb_get_ticker(self):
        print(inspect.stack()[0][3])
        result = self.coinone.get_ticker(currency_type="BTC")
        assert result is not None
        print(result)

    def tearDown(self):
        pass