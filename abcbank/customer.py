from account import CHECKING, SAVINGS, MAXI_SAVINGS 
class Customer: 
	def __init__(self, name): 
		self.name = name 
		self.totalBalance = 0
		self.accounts = [] 

	def openAccount(self, account): 
		self.accounts.append(account) 
		return self 

	# Transfer amount from account1 to account2, by Liwen Guo
	def transferBetweenAccounts(self, amount, account1, account2): 
		self.accounts[account1].withdraw(amount)
		self.accounts[account2].deposit(amount)		
		return self 

	def getTotalBalance:
		totalBalance = 0
		for account in self.accounts:
			totalBalance += account.balance
		return totalBalance
		
	def numAccs(self): 
		return len(self.accounts) 

	def totalInterestEarned(self): 
		return sum([a.interestEarned() for a in self.accounts]) 

	# This method gets a statement 
	def getStatement(self): 
		# JIRA-123 Change by Joe Bloggs 29/7/1988 start 
		statement = None  # reset statement to null here 
		# JIRA-123 Change by Joe Bloggs 29/7/1988 end 
		totalAcrossAllAccounts = self.getTotalBalance() 
		statement = "Statement for %s" % self.name 
		for account in self.accounts: 
			statement = statement + self.statementForAccount(account) 
		statement = statement + "\n\nTotal In All Accounts " + _toDollars(totalAcrossAllAccounts) 
		return statement 

	def statementForAccount(self, account): 
		accountType = "\n\n\n" 
		if account.accountType == CHECKING: 
			accountType = "\n\nChecking Account\n" 
		if account.accountType == SAVINGS: 
			accountType = "\n\nSavings Account\n" 
		if account.accountType == MAXI_SAVINGS: 
			accountType = "\n\nMaxi Savings Account\n" 
		transactionSummary = [self.withdrawalOrDepositText(t) + " " + _toDollars(abs(t.amount)) for t in account.transactions] 
		transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n" 
		totalSummary = "Total " + _toDollars(account.balance) 
		return accountType + transactionSummary + totalSummary 

	def statementWithDateForAccount(self, account): 
		accountType = "\n\n\n" 
		if account.accountType == CHECKING: 
			accountType = "\n\nChecking Account\n" 
		if account.accountType == SAVINGS: 
			accountType = "\n\nSavings Account\n" 
		if account.accountType == MAXI_SAVINGS: 
			accountType = "\n\nMaxi Savings Account\n" 
		transactionSummary = [self.withdrawalOrDepositText(t) + " " + _toDollars(abs(t.amount)) + " on " + str(t.transactionDate) for t in account.transactions] 
		transactionSummary = "  " + "\n  ".join(transactionSummary) + "\n" 
		totalSummary = "Total " + _toDollars(account.balance) 
		return accountType + transactionSummary + totalSummary 

	def withdrawalOrDepositText(self, transaction): 
		if transaction.amount < 0: 
			return "withdrawal" 
		elif transaction.amount > 0: 
			return "deposit" 
		else: 
			return "N/A" 

def _toDollars(number): 
	return "${:1.2f}".format(number) 
