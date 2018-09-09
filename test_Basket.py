import pytest
from Basket import Basket
from Item import Item

@pytest.fixture(scope="module")
def empty_basket():
	return Basket()

@pytest.fixture(scope="module")
def book():
	return Item("Of Mice and Men", "Paperback, Of Mice and Men, Steinbeck", "book_OMaM_01", 8.99)

@pytest.fixture(scope="module")
def dvd():
	return Item("Fellowship of the Ring", "Lord of the Rings, Fellowship of the Ring", "DVD_FotR_1", 9.99)

@pytest.fixture(scope="module")
def basket_one_item(book):
	items = [book]
	return Basket(items)

def test_can_instantiate_basket(empty_basket):
	assert empty_basket

def test_can_instantiate_basket_with_one_item(basket_one_item):
	assert basket_one_item

def test_basket_contains_item(basket_one_item, book):
	assert basket_one_item.is_item_in_basket(book)

def test_empty_basket_can_add_item(empty_basket, book):
	empty_basket.add_item(book)
	assert empty_basket.is_item_in_basket(book)

def test_basket_with_one_item_can_add_another(basket_one_item, dvd):
	basket_one_item.add_item(dvd)
	assert basket_one_item.is_item_in_basket(dvd)
