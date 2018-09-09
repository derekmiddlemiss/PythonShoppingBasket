class StockController:

	@staticmethod
	def get_stock_code_from_item(item):
		try:
			stock_code = item.stock_code
			return stock_code
		except AttributeError:
			print("Object " + str(item) " has no stock_code")
			return None

	def __init__(self, items = None):
		self.stock_count = {}
		for item in items:
			self.add_stock_item(item)

	def add_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code not None:
			if code not in self.stock_count:
				self.stock_count[code] = 1
			else:
				self.stock_count[code] += 1

	def remove_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code not None: 
			if code not in self.stock_count:
				raise RuntimeError("Stock code for this item not present in stock count")
			elif self.stock_count[code] > 1:
				# Reduce count by 1, but still remaining stock for this code
				self.stock_count[code] -= 1
			else:
				# Last stock item removed
				self.stock_count.pop(code)

	def get_stock_count_for_code(self, code):
		if code in self.stock_count:
			return self.stock_count[code]
		else:
			return 0
