import unittest
from project1.project1 import TimeZone, Account
from datetime import timedelta


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_number = 'A100'
        self.first_name = 'JY'
        self.last_name = 'Lee'
        self.tz = TimeZone('TZ', 1, 30)
        self.balance = 100.00

    def create_account(self):
        return Account(self.account_number, self.first_name, self.last_name, self.tz, self.balance)

    def test_create_timezone(self):
        tz = TimeZone('KST', 9, 0)
        self.assertEqual('KST', tz.name)
        self.assertEqual(timedelta(hours=9, minutes=0), tz.offset)

    def test_timezone_equal(self):
        tz1 = TimeZone('ABC', -1, -30)
        tz2 = TimeZone('ABC', -1, -30)
        self.assertEqual(tz1, tz2)

    def test_timezone_not_equal(self):
        tz = TimeZone('ABC', -1, -30)

        test_timezones = (
            TimeZone('DEF', -1, -30),
            TimeZone('ABC', -1, 0),
            TimeZone('ABC', 1, -30)
        )

        for i, test_tz in enumerate(test_timezones):
            with self.subTest(test_number=f'Test # {i}'):
                self.assertNotEqual(tz, test_tz)

    def test_create_account(self):
        a = self.create_account()

        self.assertEqual(self.account_number, a.account_number)
        self.assertEqual(self.first_name, a.first_name)
        self.assertEqual(self.last_name, a.last_name)
        self.assertEqual(self.first_name + ' ' + self.last_name, a.full_name)
        self.assertEqual(self.tz, a.timezone)
        self.assertEqual(self.balance, a.balance)

    def test_create_account_blank_first_name(self):
        self.first_name = ''

        with self.assertRaises(ValueError):
            a = self.create_account()

    def test_create_negative_balance(self):
        self.balance = -100.00

        with self.assertRaises(ValueError):
            a = self.create_account()

    def test_account_withdraw_ok(self):

        a = self.create_account()
        conf_code = a.withdraw(20)
        self.assertTrue(conf_code.startswith('W-'))
        self.assertEqual(self.balance - 20, a.balance)

    def test_account_withdraw_overdraw(self):
        a = self.create_account()
        conf_code = a.withdraw(200)
        self.assertTrue(conf_code.startswith('X-'))
        self.assertEqual(self.balance, a.balance)


if __name__ == '__main__':
    run_tests(TestAccount)
