import unittest, os
from src.bank_accout import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        
        new_balance = self.account.deposit(500)
#        assert new_balance == 1500
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw(self):
        
        new_balance = self.account.withdraw(200)
#        assert new_balance == 800
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance(self):      
#        assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transaction_log(self):
        self.account.deposit(500)
#        assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    def test_deposit_multiple_ammounts(self):
        test_cases=[
            {"ammount" : 100, "expected": 1100},
            {"ammount" : 3000, "expected": 4000},
            {"ammount" : 4500, "expected": 5500}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])