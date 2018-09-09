class Item:

	__stock_count = {}

	def __init__(self, name, desc, stock_code, price):
		self.name = name
		self.desc = desc
		self.stock_code = stock_code
		self.price = price
		Item.add_stock_item(self)

	@classmethod
	def add_stock_item(cls, item):
		key = item.stock_code
		if key not in cls.__stock_count:
			cls.__stock_count[key] = 1
		else:
			cls.__stock_count[key] += 1

	@classmethod
	def remove_stock_item(cls, item):
		key = item.stock_code
		if key not in cls.__stock_count:
			raise RuntimeError("Item not logged in stock count")
		elif cls.__stock_count[key] > 1:
			cls.__stock_count[key] -= 1
		else:
			cls.__stock_count.pop(key)

	@classmethod
	def get_stock_count_for_code(cls, code):
		if code in cls.__stock_count:
			return cls.__stock_count[code]
		else:
			return 0



