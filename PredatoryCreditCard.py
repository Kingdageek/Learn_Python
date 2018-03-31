#PredatoryCreditCard.py
from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    SURCHARGE = 1
    
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr  # Annual Percentage Rate
        self._count = 0

    def charge(self, price):
        """
        Specialize the charge method in the CreditCard superclass.
        If the superclass's charge() returns True, return True. if
        it returns False, add $5 to balance/debt
        """
        self._count += 1
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success

    def process_month(self):
        """
        Interest to be charged on balance/debt monthly.
        Using compound interest.
        Amount = principal(1 + R(in 1 yr))**time(in years)
        1/12 implies a month.
        If the charge method was called more than 10 times that month,
        charge a $1 fee according to the number of times more that 10.
        set count back to zero.
        """
        self._balance = self._balance * ((1 + self._apr) ** (1/12))
        if self._count > 10:
            temp = self._count - 10
            self._balance += PredatoryCreditCard.SURCHARGE * temp
        self._count = 0
        
