from typing import List

class Product:
    
    __slot__ = ["__name", "__id", "__price", "__weight"]

    def __init__(self, id: int, name: str, weight: float, price: float) -> None:
        self.__name = name
        self.__id = id
        self.__price = price
        self.__weight = weight
    
    def __str__(self) -> str:
        return str(self.__id)

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        self.__price = value
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, value: float) -> None:
        self.__weight = value


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


class ShoppingList:
    
    __slots__ = ["__name", "__containers"]

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__containers: List[Container] = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def totalItems(self) -> int:
        total = 0
        for container in self.__containers:
            total += container.units
        return total
    
    @property
    def totalPrice(self) -> float:
        totalPrice = 0
        for container in self.__containers:
            totalPrice += container.totalPrice
        return totalPrice
    
    def add_item(self, product: Product) -> None:
        if isinstance(product, Product):
            contains = False
            for container in self.__containers:
                if container.product == product:
                    container.increase()
                    contains = True
                    break
            if not contains:
                self.__containers.append(Container(product))
        else:
            raise TypeError(f"Object '{product}' is not an instance of Product")
    
    def remove_item(self, product: Product) -> bool:
        if isinstance(product, Product):
            for container in self.__containers:
                if container.product == product:
                    self.__containers.remove(container)
                    return True
            return False
        else:
            raise TypeError(f"Object '{product}' is not an instance of Product")
        
    def getItem(self, product: Product) -> Product:
        if isinstance(product, Product):
            for container in self.__containers:
                if container.product == product:
                    return True
            return False
        else:
            raise TypeError(f"Object '{product}' is not an instance of Product")
        
    def printList(self):
        output = f"\nName list: {self.__name}\nTotal products: {self.totalItems}\nProducts: "
        for container in self.__containers:
            output += f"\n\t{container.product.name} - R$ {container.product.price} * ({container.units}) = RS {container.totalPrice}"
        output += f"\nTotal price: R$ {self.totalPrice}"
        print(output)