from datetime import datetime
from stock_alerter.stock import Stock
from stock_alerter.rule import PriceRule


exchange = {"GOOG": Stock("GOOG"), "MSFT": Stock("MSFT")}

rule = PriceRule("MSFT", lambda dupa: dupa.price > 100)

print(rule.matches(exchange))

exchange["GOOG"].update(datetime(2014, 2, 13), 50)

print(rule.matches(exchange))

exchange["MSFT"].update(datetime(2014, 2, 13), 101)

print(rule.matches(exchange))
