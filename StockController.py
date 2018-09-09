class StockController:

	@staticmethod
	def get_stock_code_from_item(item):
		try:
			stock_code = item.stock_code
			return stock_code
		except AttributeError:
			print("Object " + str(item) + " has no stock_code")
			return None

	def __init__(self, items = None):
		self.stock_count = {}
		if items is not None:
			messages = []
			for item in items:
				messages.append(self.add_stock_item(item))
			return messages

	def add_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code is not None:
			if code not in self.stock_count:
				self.stock_count[code] = 1
			else:
				self.stock_count[code] += 1
			return "Item added"
		return "Item not added"

	def remove_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code is not None: 
			if code in self.stock_count:
				if self.stock_count[code] > 1:
					# Reduce count by 1, but there are still remaining items with this code
					self.stock_count[code] -= 1
				else:
					# Last item with this code removed, remove code from dict
					self.stock_count.pop(code)
				return "Item removed"
		return "Item not removed"

	def get_stock_count_for_code(self, code):
		if code in self.stock_count:
			return self.stock_count[code]
		else:
			return 0
