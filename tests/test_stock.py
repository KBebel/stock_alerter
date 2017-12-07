import unittest
from datetime import datetime
from stock_alerter.stock import Stock


class StockTest(unittest.TestCase):

    def setUp(self):
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp """

        self.goog.update(datetime(2017, 11, 30), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):

        # try:
        #     goog.update(datetime(2017, 11, 30), price=-1)
        # except ValueError:
        #     return
        # self.fail("ValueError was not raised")
        self.assertRaises(ValueError, self.goog.update,
                          datetime(2017, 11, 30), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2017, 11, 29), price=8)
        self.goog.update(datetime(2017, 11, 30), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)

    def test_price_is_the_latest_even_if_updates_are_made_out_of_order(self):
        self.goog.update(datetime(2014, 2, 13), price=8)
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(8, self.goog.price)





class StockTrendTest(unittest.TestCase):

    def setUp(self):
        self.goog = Stock("GOOG")

    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 11), \
                      datetime(2014, 2, 12), \
                      datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)


    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases_for_3_updates(self):
        self.given_a_series_of_prices([8, 12, 10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal_for_3_updates(self):
        self.given_a_series_of_prices([8, 8, 8])
        self.assertFalse(self.goog.is_increasing_trend())


if __name__ == "__main__":
    unittest.main()