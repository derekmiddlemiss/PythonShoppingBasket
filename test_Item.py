import pytest
from Item import Item

@pytest.fixture(scope="module")
def dvd_SoaP():
	return Item("Snakes on a Plane", "DVD of Snakes on a Plane", "DVD_SoaP_1", 2.99)

def test_can_instantiate_item(dvd_SoaP):
	assert dvd_SoaP

def test_item_has_name(dvd_SoaP):
	assert dvd_SoaP.name == "Snakes on a Plane"

def test_item_has_price(dvd_SoaP):
	assert dvd_SoaP.price == pytest.approx(2.99)

def test_item_has_desc(dvd_SoaP):
	assert dvd_SoaP.desc == "DVD of Snakes on a Plane"

def test_item_has_stock_code(dvd_SoaP):
	assert dvd_SoaP.stock_code == "DVD_SoaP_1"

def test_item_added_to_stock_count(dvd_SoaP):
	# this should be true given module scope for fixture, dvd_SoaP created only once per module
	assert Item.get_stock_count_for_code(dvd_SoaP.stock_code) == 1

def test_deleted_item_removed_from_stock_count(dvd_SoaP):
	Item.remove_stock_item(dvd_SoaP)
	assert Item.get_stock_count_for_code(dvd_SoaP.stock_code) == 0

