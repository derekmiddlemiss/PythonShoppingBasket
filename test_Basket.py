import pytest
from Basket import Basket

@pytest.fixture(scope="module")
def empty_basket():
	return Basket()

def test_can_instantiate_basket(empty_basket):
	assert empty_basket