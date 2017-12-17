import unittest
from unittest import mock
from datetime import datetime

from stock_alerter.alert import Alert
from stock_alerter.rule import PriceRule
from stock_alerter.stock import Stock
from stock_alerter.event import Event


# class TestAction:
#     executed = False

#     def execute(self, description):
#         self.executed = True


class AlertTest(unittest.TestCase):
    def test_action_is_executed_when_rule_matches(self):
        exchange = {"GOOG": Stock("GOOG")}
        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        action.execute.assert_not_called()
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with("sample alert")

if __name__ == '__main__':
    unittest.main()
