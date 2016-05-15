from nose.tools import assert_equals, nottest

from account import Account, CHECKING, SAVINGS
from customer import Customer


def test_statement(name, accounts, transactions): 
	customer = Customer(name)
	stmt = None;
	for i, account in enumerate(accounts):
		customer.openAccount(account)
		if account.accountType == CHECKING：
			atype = "Checking"
		elif account.accountType == SAVINGS：
			atype = "Saving"
		elif account.accountType == MAXI_SAVINGS：
			atype = "Maxi Savings"
		stmt += "\n\n“ + atype + " Account\n"
		for transaction in transactions[i]
			if transaction.amount > 0:
				account.deposit(amount)
				stmt += " deposit " + _toDollars(abs(amount)) 
			elif transaction.amount < 0:
				account.withdraw(-amount)
				stmt += " withdraw " + _toDollars(abs(amount)) 
		stmt += "\nTotal" + _toDollars(abs(account.balance))
	stmt += "\n\nTotal In All Accounts " + _toDollars(customer.getTotalBalance())
	
	assert_equals(henry.getStatement(), stmt) 

def test_statement_call():
	name = "Henry"
	anum = 12345
	accounts = []
	atypes = [CHECKING, SAVINGS, MAXI_SAVINGS]
	for atype in atypes):
		account = Account(anum, atype)
		accounts.append(account)
	camount = [100, -50, -30]
	samount = [100, -50, 10]
	mamount = [1000, 500, -2000]
	transactions = [amount, smount, mmount]
	test_statement(name, accounts, transactions)

def test_multipleAccount(customerName, accounts): 
	customer = Customer(customerName)
	for account in accounts:
		customer.openAccount(account) 
	assert_equals(customer.numAccs(), len(accounts)) 

def test_multipleAccount_call(): 
	name = "John"
	anum = 12345
	accounts = []
	atypes = [CHECKING, SAVINGS, MAXI_SAVINGS, 10， None]
	for atype in atypes):
		account = Account(anum, atype)
		accounts.append(account)
	test_multipleAccount(name, accounts)
