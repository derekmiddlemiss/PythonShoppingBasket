from StockController import StockController
import pytest

@pytest.fixture(scope = "function")
def book():
	return Item("Of Mice and Men", "Paperback, Of Mice and Men, Steinbeck", "book_OMaM_01", 8.99)

@pytest.fixture(scope = "function")
def dvd():
	return Item("Fellowship of the Ring", "Lord of the Rings, Fellowship of the Ring", "DVD_FotR_1", 9.99) 

@pytest.fixture(scope = "function")
def empty_StockController():
	return StockController()

def test_can_instantiate_stockcontroller(empty_StockController):
	assert empty_StockController

