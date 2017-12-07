class Rule:

    def __init__(self, symbol, condition):
        self.symbol = symbol
        self.condition = condition

    def match(self, what):
        this = what[self.symbol]
        return self.condition(this)


class Function:

    def __init__(self, symbol):
        self.symbol = symbol
        self.result = None


funkcja = {"division": Function("division")}

nowaf = Function("mnozenie")

print(nowaf.symbol)

newrule = Rule("mnozenie", lambda Func: Func.result > 2)

nowaf.result = 1

print(nowaf.result)

zespol = {"mnozenie": nowaf}

print(newrule.match(zespol))


# funkcja["division"].result = 4

# print(funkcja["division"].result)

# print(newrule.match(funkcja))
