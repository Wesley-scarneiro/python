from codes.product import Product

class Container:
    
    __slots__ = ["__product", "__units"]

    def __init__(self, product: Product) -> None:
        self.__product = product
        self.__units = 1
    
    @property
    def product(self) -> Product:
        return self.__product
    
    @property
    def units(self) -> int:
        return self.__units
    
    @property
    def totalPrice(self) -> float:
        return self.__units * self.__product.price
    
    def increase(self) -> None:
        self.__units += 1

    def decrease(self) -> None:
        if self.__units > 1:
            self.__units -= 1
