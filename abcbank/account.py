from abcbank.transaction import Transaction

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []
        self.latestWithdrawDate		# Added by liwenguo123
        
    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))
            self.latestWithdrawDate = DateProvider.today();		# Added by liwenguo123

    def interestEarned(self):
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002
        if self.accountType == MAXI_SAVINGS:
            # Revised by liwenguo123 
			today = DateProvider.today()
			withdrawPassedDays = today - self.latestWithdrawDate;
			listDaysStr = str(withdrawPassedDays).split()
			numDays = int(listDaysStr)
			if (numDays > 10):
				return amount * 0.05
			else:
				return amount * 0.001            
            #if (amount <= 1000):
            #    return amount * 0.02
            #elif (amount <= 2000):
            #    return 20 + (amount - 1000) * 0.05
            #else:
            #    return 70 + (amount - 2000) * 0.1
        else:
            return amount * 0.001

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
