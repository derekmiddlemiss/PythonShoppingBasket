class Basket:

	def __init__(self, items = []):
		self.items = items

	def is_item_in_basket(self, item):
		return item in self.items

