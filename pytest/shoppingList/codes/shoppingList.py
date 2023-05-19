from codes.product import Product
from codes.container import Container
from typing import List

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
    def totalProducts(self) -> int:
        return len(self.__containers)

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
                if container.product.id == product.id:
                    container.increase()
                    contains = True
                    break
            if not contains:
                self.__containers.append(Container(product))
        else:
            raise TypeError(f"Object '{product}' is not an instance of Product")
    
    def remove_item(self, id: int) -> bool:
        if isinstance(id, int):
            for container in self.__containers:
                if container.product.id == id:
                    self.__containers.remove(container)
                    return True
            return False
        else:
            raise TypeError(f"The ID '{id}' does not a integer")
        
    def getItem(self, id: int) -> Product | None:
        if isinstance(id, int):
            for container in self.__containers:
                if container.product.id == id:
                    return container.product
            return None
        else:
            raise TypeError(f"The ID '{id}'does not a integer")
        
    def printList(self):        
        output = f"\nName list: {self.__name}\nTotal products: {self.totalItems}\nProducts: "
        for container in self.__containers:
            output += f"\n\t{container.product.name} - R$ {container.product.price} * ({container.units}) = RS {container.totalPrice}"
        output += f"\nTotal price: R$ {self.totalPrice}"
        print(output)