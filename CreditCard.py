#CreditCard.py

class CreditCard:

    def __init__(self, customer, bank, account, limit, bank_bal = 0):
        """
        Initialize instance of CreditCard.
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = bank_bal # To store customer spendings.
        
    # Class Interfaces
    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    # Methods for payment and charge processing
    def charge(self, price):
        """
        returns True if customer's current balance and 'price'
        doesn't exceed the limit on the credit card. It then
        updates the balance. It returns False if it can't be
        processed
        """
        if not isinstance(price, (int, float)):
               raise TypeError()
               
        if self._balance + price <= self._limit:
            self._balance += price
            return True
        else: return False

    def make_payment(self, amount):
        """
        Allows the customer to make a payment to the credit card
        company and reduce the balance on the credit card.
        """
        if not isinstance(amount, (int, float)):
               raise TypeError()
        if amount < 0: raise ValueError()
        self._balance -= amount

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Nonso the Great", "Bank of America",
                              "00001 01010101", 1000))
    wallet.append(CreditCard("Nonso Mgbechi", "World Bank", "0101010 0101010",
                              1000))
    wallet.append(CreditCard("Nonso Kingsley Godtime", "Bank of Technology",
                              "0100100999", 1000))
    for i in range(1,23):
        wallet[0].charge(i)
        wallet[1].charge(i *3)
        wallet[2].charge(i *2)

    for c in wallet:
        print('Customer: ', c.get_customer())
        print("Bank: ", c.get_bank())
        print("Account: ", c.get_account())
        print("Limit: ", c.get_limit())
        print("Balance: ", c.get_balance())
        while c.get_balance() > 100:
            c.make_payment(100)
            print("New Balance: ", c.get_balance())
        print()
        
