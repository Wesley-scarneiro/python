from codes.product import Product
import pytest

class TestUnitProduct:

    @pytest.fixture
    def product(self):
        return Product(1111, 'feijao', 1.0, 14.99)

    def test_str_id_12542(self):
        input = 12542 # given
        expected = '12542'
        output = Product(input, 'feijão', 1.0, 14.99) #when
        assert output.__str__()== expected #then

    def test_getName_feijao(self):
        input = 'feijão'
        expected = 'feijão'
        output = Product(12542, input, 1.0, 14.99)
        assert output.name == expected
    
    # with fixture
    def test_setName_feijaoA_feijaoB(self, product):
        input = 'feijão B'
        expected = 'feijão B'
        product.name = input
        assert product.name == expected
    
    def test_getId_1111(self):
        input = 1111
        expected = 1111
        output = Product(input, 'arroz', 1.0, 14.99) 
        assert output.id == expected 
    
    def test_getPrice_10(self):
        input = 10.0
        expected = 10.0
        output = Product(1111, 'macarrão', 0.5, input)
        assert output.price == expected
    
    def test_setPrice_10_12(self, product: Product):
        input = 12.0
        expected = 12.0
        product.price = input
        assert product.price == expected

    def test_getWeight_5(self):
        input = 5.0
        expected = 5.0
        output = Product(1111, 'arroz', input, 10.0)
        assert output.weight == expected
    
    def test_setWeight_5_4(self, product: Product):
        input = 4.0
        expected = 4.0
        product.weight = input
        assert product.weight == expected
