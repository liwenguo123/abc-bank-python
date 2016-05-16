from nose.tools import assert_equals 

from account import Account, CHECKING, MAXI_SAVINGS, SAVINGS 
from bank import Bank 
from customer import Customer 
 
def test_customer_summary(name, accountNo， accountType): 
	bank = Bank() 
	numAcc = len(accountNo)
	for anum, atype in zip(accountNo, accountType):
		customer = Customer(name).openAccount(Account(anum, atype)) 
	bank.addCustomer(customer) 
	assert_equals(bank.customerSummary(), "Customer Summary\n - %s (%d (account if (numAcc == 1) else accounts)" %(name, numAcc)) 

def test_customer_summary_call():
	names = ["John", "John", "Jone", "Jone", None]
	accNos = [1234, 1235, 1236， 1237, None]
	accTypes = [CHECKING, SAVINGS, MAXI_SAVINGS, 10， None]
	
	for name, anum, atype in zip(names, accNos, accTypes):
		test_customer_summary(name, anum, atype)

	name = "john"
	del accNos[:]
	accNos.append(123)
	accNos.append(456)
	del accTypes[:]
	accTypes.append(CHECKING)
	accTypes.append(SAVINGS)
	test_customer_summary(name, accNos, accTypes)
	
def test_account(name, account, depositAmounts, withdrawAmounts): 
	bank = Bank() 
	customer = Customer(name).openAccount(account) 
	bank.addCustomer(customer)
	for damount in depositAmounts:
		account.deposit(damount) 
	for wamount in withdrawAmounts:
		account.withdraw(damount)
	interest = 0;
	if account.accountType == CHECKING:
		interest = 0.1
	elif account.accountType == SAVINGS:
		interest = 0.1
	elif account.accountType == MAXI_SAVINGS:
		interest = 0.5
	assert_equals(bank.totalInterestPaid(), interest) 

def test_account_call(): 
	name = "John"
	anum = 12345
	atypes = [CHECKING, SAVINGS, MAXI_SAVINGS, 10， None]
	damount = [100, 0, -30, 100]
	wamount = [50, 0, -20, 1000]
	for atype in atypes:
		account = Account(anum, atype)
		test_account(name, account, damount, wamount)
		
