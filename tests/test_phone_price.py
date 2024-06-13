import unittest

from func.phone_price import get_cheapest_operator


class TestGetCheapestPrice(unittest.TestCase):
    def test_with_case_return_value(self):
        operator_prices = {
            "operator_a": {
                 "1": 0.9,
                 "46": 0.17,
                 "268": 5.1,
                 "468": 0.15,
                 "4620": 0,
                 "4631": 0.15,
                 "4673": 0.9,
                 "46732": 1.1
            },
            "operator_b": {
                "1": 0.92,
                "44": 0.5,
                "46": 0.2,
                "48": 1.2,
                "467": 1
            }
        }
        phone_number = "4673212345"
        # With provide input, we expect func will return the cheapest price is 1 with operator_b
        expected_result = {"operator_b": 1}
        self.assertEqual(get_cheapest_operator(operator_prices, phone_number), expected_result)

    def test_with_case_return_none_value(self):
        operator_prices = {
            "operator_a": {
                "1": 0.9,
                "46": 0.17,
                "268": 5.1,
                "468": 0.15,
                "4620": 0,
                "4631": 0.15,
                "4673": 0.9,
                "46732": 1.1
            },
            "operator_b": {
                "1": 0.92,
                "44": 0.5,
                "46": 0.2,
                "48": 1.2,
                "467": 1
            }
        }
        phone_number = "9467321234"
        # With provide input, cannot find any match prefix of phone_number so result will be None
        self.assertIsNone(get_cheapest_operator(operator_prices, phone_number))
