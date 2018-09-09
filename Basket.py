class Basket:

	def __init__(self, items = []):
		self.items = items

	def is_item_in_basket(self, item):
		return item in self.items

	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		try:
			self.items.remove(item)
		except ValueError:
			return "Item not in basket"

	def empty_basket(self):
		self.items = []


