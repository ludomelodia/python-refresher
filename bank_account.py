class Bankaccount: 
    def __init__(self, name, num)
        self._balance = 0
        self._name = name
        self._acct_num = num

    def withdraw(self, amt)
        if amt <= self._balance
            self._balance = self._balance - amt
            return

    def deposit(self, amt)
        self._balance = self._balance + amt
        return

    def current_balance(self)
        return self._balance