from unittest import mock


class PrintAction:
    def run(self, description):
        print("{} was executed".format(description))

mock1 = mock.Mock()
print(mock1.execute("sample alert"))
print(mock1.sssij())

mock2 = mock.Mock(spec=PrintAction)
# mock2.execute("sample alert")
