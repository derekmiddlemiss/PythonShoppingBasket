from StockController import StockController
from Item import Item
import pytest

@pytest.fixture(scope = "function")
def book():
	return Item("Of Mice and Men", "Paperback, Of Mice and Men, Steinbeck", "book_OMaM_01", 8.99)

@pytest.fixture(scope = "function")
def dvd():
	return Item("Fellowship of the Ring", "Lord of the Rings, Fellowship of the Ring", "DVD_FotR_1", 9.99) 

@pytest.fixture(scope = "function")
def empty_stock_controller():
	return StockController()

@pytest.fixture(scope = "function")
def stock_controller_one_item(book):
	items = [book]
	return StockController(items)

def test_can_instantiate_stockcontroller(empty_stock_controller):
	assert empty_stock_controller

def test_can_instantiate_stockcontroller_one_item(stock_controller_one_item):
	assert stock_controller_one_item

def test_stock_count_correct_for_one_item(stock_controller_one_item, book):
	assert stock_controller_one_item.get_stock_count_for_code(book.stock_code) == 1

def test_stockcontroller_can_add_item(stock_controller_one_item, dvd):
	stock_controller_one_item.add_stock_item(dvd)
	assert stock_controller_one_item.get_stock_count_for_code(dvd.stock_code) == 1

def test_stockcontroller_can_remove_item(stock_controller_one_item, book):
	stock_controller_one_item.remove_stock_item(book)
	assert stock_controller_one_item.get_stock_count_for_code(book.stock_code) == 0

def test_total_stock_count_for_one_item(stock_controller_one_item):
	assert stock_controller_one_item.get_total_stock_count() == 1

def test_stock_controller_will_not_add_object_without_stockcode(stock_controller_one_item):
	stock_controller_one_item.add_stock_item("not_an_Item")
	assert stock_controller_one_item.get_total_stock_count() == 1	

