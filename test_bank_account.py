import unittest
from bank_account import Bankaccount

class TestBank(unittest.Testcase)
    def setUp(self):
        self.myAccount = Bankaccount("Ludo", "0000")
    def test_name(self):
        self.assertAlmostEqual(self._name, "Ludo")
    def test_account_number(self):
    def test_initial_balance(self):
    def test_withdraw(self):
    def test_deposit(self):
    def test_current_balance(self):
