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