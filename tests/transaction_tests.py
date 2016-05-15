from nose.tools import assert_is_instance

from transaction import Transaction


def test_type(amount): 
	t = Transaction(amount) 
	assert_is_instance(t, Transaction, "correct type") 

def test_type_call(): 
	amounts = [5, 1000, -200, None]
	for amount in amounts:
		test_type(amount)
