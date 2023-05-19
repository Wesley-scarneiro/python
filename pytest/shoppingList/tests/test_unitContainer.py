from codes.container import Container
from codes.product import Product

import pytest
'''
    Corrigir input e output para variáveis mais simples e corretas
'''
class TestUnitContainer:

    @pytest.fixture
    def product(self):
        return Product(12543, 'produtoDeTeste', 1.0, 9.99)
    
    def test_getProduct_type_product(self, product):
        expected = Product
        output = Container(product)
        assert type(output.product) is expected

    def test_units_1_1(self, product):
        expected = 1
        output = Container(product)
        assert output.units == expected
    
    def test_totalPrice_99_9(self, product):
        expected = 99.9
        container = Container(product)
        for i in range(9):
            container.increase()
        assert container.totalPrice == expected

    def test_increase_1_2(self, product):
        expected = 2
        output = Container(product)
        output.increase()
        assert output.units == expected
    
    def test_increase_100_101(self, product):
        expected = 101
        output = Container(product)
        for i in range(100):
            output.increase()
        assert output.units == expected
    
    def test_decrease_1_1(self, product):
        expected = 1
        output = Container(product)
        output.decrease()
        assert output.units == expected
    
    def test_decrease_1_3(self, product):
        expected = 3
        output = Container(product)
        for i in range(3):
            output.increase()
        output.decrease()
        assert output.units == expected

    def test_decrease_3_1(self, product):
        expected = 1
        output = Container(product)
        for i in range(3):
            output.increase()
        for i in range(3):
            output.decrease()
        assert output.units == expected

    def test_raise_exception_AttributeError(self, product):
        with pytest.raises(AttributeError) as e:
            container = Container(product)
            container.novoAtributo = 10
        assert str(e.value) == "'Container' object has no attribute 'novoAtributo'"
