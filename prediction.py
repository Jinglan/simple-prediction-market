# Jinglan Wang


class Token:
	# Default initial allocation to empty dict
	def __init__(self, initial_allocation = {}):
		self.initial_allocation = initial_allocation
		self.balances = initial_allocation

	def mint(self, owner, amount):
		# If this account doesn't exist, create a new one
		if owner not in self.balances:
			self.balances[owner] = 0
		self.balances[owner] += amount

	def transfer(self, sender, recipient, amount):
		assert self.balances[sender] >= amount and amount > 0
		if recipient not in self.balances:
			self.balances[recipient] = 0
		self.balances[sender] -= amount
		self.balances[recipient] += amount

# Initialize a new prediction market
class PredictionMarket():
	def __init__(self):
		self.outcomeA
		self.outcomeB

	def vote():
		blah

# Tests
def test_token():
	#initialize
	ces = Token()
	ces.mint("Karl", 5)
	ces.transfer("Karl", "Jing", 3)
	assert ces.balances == {"Karl": 2, "Jing": 3}
	print(ces.balances)

test_token()