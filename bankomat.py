class CashMachine:

    def __init__(self):
        self.__bills = []

    def put_money(self, bills):

        self.__bills.extend(bills)

    @property
    def is_available(self):
        return bool(self.__bills)

    def withdraw_money(self, amount):

        to_withadraw = []

        for bill in sorted(self.__bills, reverse=True):
            if sum(to_withadraw) + bill <= amount:
                to_withadraw.append(bill)

        if sum(to_withadraw) == amount:
            for bill in to_withadraw:
                self.__bills.remove(bill)
            return to_withadraw

        return []

    def state(self):
        return self.__bills


cash_machine = CashMachine()
cash_machine.is_available
cash_machine.put_money([200, 100, 100, 50])
assert cash_machine.is_available

print(cash_machine.withdraw_money(500))

print(cash_machine._CashMachine__bills)