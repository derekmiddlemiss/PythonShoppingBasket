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
			for item in items:
				self.add_stock_item(item)

	def add_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code is not None:
			if code not in self.stock_count:
				self.stock_count[code] = 1
			else:
				self.stock_count[code] += 1
		else:
			print("Object " + str(item) + " not added")


	def remove_stock_item(self, item):
		code = StockController.get_stock_code_from_item(item)
		if code is not None: 
			if code in self.stock_count:
				self.stock_count[code] -= 1
				if self.stock_count[code] == 0:
					self.stock_count.pop(code)
			else:
				print("Item not in stock count")
		else:
			print("Object " + str(item) + " not removed")


	def get_stock_count_for_code(self, code):
		if code in self.stock_count:
			return self.stock_count[code]
		else:
			return 0

	def get_total_stock_count(self):
		total_count = 0
		for key in self.stock_count.keys():
			total_count += self.stock_count[key]
		return total_count

