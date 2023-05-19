from codes.shoppingList import ShoppingList
from codes.product import Product

import pytest

class TestShoppingList:

    @pytest.fixture(scope='class')
    def shoppingList(self):
        return ShoppingList('Shopping month')
    
    def test_name_Shopping_month(self, shoppingList):
        expected = 'Shopping month'
        assert shoppingList.name == expected
    
    def test_total_items_zero(self, shoppingList):
        expected = 0
        assert shoppingList.totalItems == expected

    def test_total_products_zero(self, shoppingList):
        expected = 0
        assert shoppingList.totalProducts == expected
    
    def test_total_price_zero(self, shoppingList):
        expected = 0.0
        assert shoppingList.totalPrice == expected

    def test_add_products_one(self, shoppingList):
        expected = 1
        shoppingList.add_item(Product(1254, 'Product-testA', 2.5, 10.99))
        assert shoppingList.totalProducts == expected
    
    def test_add_products_three(self, shoppingList):
        expected = 3
        shoppingList.add_item(Product(1258, 'Product-testA', 2.5, 10.99))
        shoppingList.add_item(Product(1111, 'Product-testB', 2.5, 10.99))
        assert shoppingList.totalProducts == expected
    
    def test_total_items_three(self, shoppingList):
        expected = 3
        assert shoppingList.totalItems == expected
    
    def test_total_price_three_products(self, shoppingList):
        expected = 32.97
        assert shoppingList.totalPrice == expected
    
    def test_add_products_one_hundred(self, shoppingList):
        expected = 103
        for i in range(100):
            shoppingList.add_item(Product(1325+i, 'Product-test'+str(i), 2.5, 10.99))
        assert shoppingList.totalProducts == expected

    def test_total_items_one_hundred(self, shoppingList):
        expected = 103
        assert shoppingList.totalItems == expected
    
    def test_getItem_product_1327(self, shoppingList):
        _input = 1327
        expected = 1327
        product = shoppingList.getItem(_input)
        assert product.id == expected
    
    def test_getItem_product_none(self, shoppingList):
        _input = 8795
        expected = None
        product = shoppingList.getItem(_input)
        assert product == expected

    def test_remove_products_one_hundred(self, shoppingList):
        expected = 3
        for i in range(100):
            shoppingList.remove_item(1325+i)
        assert shoppingList.totalProducts == expected

    def test_remove_products_doesnot_exist(self, shoppingList):
        _input = 9999
        expected = False
        assert shoppingList.remove_item(_input) == expected
    
    def test_total_items_3_after_remove_one_hundred(self, shoppingList):
        expected = 3
        assert shoppingList.totalItems == expected
    
    def test_add_item_existing_product_1111(self, shoppingList):
        _input = shoppingList.getItem(1111)
        expected_products = 3
        expected_items = 4
        shoppingList.add_item(_input)
        assert shoppingList.totalItems == expected_items
        assert shoppingList.totalProducts == expected_products

    def test_exception_typeError_add_item(self, shoppingList):
        _input = 1425
        with pytest.raises(TypeError) as e:
            shoppingList.add_item(_input)
            assert str(e.value) == f"Object '{_input}' is not an instance of Product"
    
    def test_exception_typeError_getItem(self, shoppingList):
        _input = '8966'
        with pytest.raises(TypeError) as e:
            shoppingList.getItem(_input)
            assert str(e.value) == f"The ID '{_input}' does not a integer"

    def test_exception_typeError_getItem(self, shoppingList):
        _input = '8966'
        with pytest.raises(TypeError) as e:
            shoppingList.getItem(_input)
            assert str(e.value) == f"The ID '{_input}' does not a integer"

    def test_exception_typeError_remove_item(self, shoppingList):
        _input = '8966'
        with pytest.raises(TypeError) as e:
            shoppingList.remove_item(_input)
            assert str(e.value) == f"The ID '{_input}' does not a integer"
