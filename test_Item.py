import pytest
from Item import Item

@pytest.fixture()
def dvd_SoaP():
	return Item("Snakes on a Plane", "DVD of Snakes on a Plane", "DVD_SoaP_1", 2.99)

def test_item_has_name(dvd_SoaP):
	assert dvd_SoaP.name == "Snakes on a Plane"

def test_item_has_price(dvd_SoaP):
	assert dvd_SoaP.price == pytest.approx(2.99)

