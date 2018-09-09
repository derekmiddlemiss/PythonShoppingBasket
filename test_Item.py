import pytest
from Item import Item

@pytest.fixture(scope = "module")
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

