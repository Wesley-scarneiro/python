from collections.abc import MutableSequence
from typing import List

class Cars:
    
    def __init__(self, model, number):
        self.__model = model
        self.__number = number

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return str(self.__number)
    
    def __lt__(self, other):
        return self.__number < other.number
    
    def __gt__(self, other):
        return self.__number > other.number


class ListCars(MutableSequence):
    
    def __init__(self, default=None):
        self.__data = []
        super().__init__()
        if default:
            for i in default:
                self.append(i)

    @property
    def data(self):
        return self.__data
    
    def __len__(self) -> int:
        return len(self.__data)
    
    def __getitem__(self, index: int):
        if index < len(self.__data):
            return self.__data[index]
        else:
            raise IndexError("index outside array bounds")

    def __setitem__(self, index, value):
        if index < len(self.__data):
            if isinstance(value, Cars):
                self.__data[index] = value
            else:
                raise TypeError(f"This list not support the type '{type(value)}'")
        else:
            raise IndexError("index outside array bounds")
    
    def insert(self, index, value):
        if index < len(self.__data):
            if isinstance(value, Cars):
                self.__data.insert(index, value)
            else:
                raise TypeError(f"This list not support the type '{type(value)}'")
        else:
            raise IndexError("index outside array bounds")
    
    def append(self, value):
        if isinstance(value, Cars):
            self.__data.append(value)
        else:
            raise TypeError(f"This list not support the type '{type(value)}'")
        
    def __delitem__(self, index):
        if index < len(self.__data):
           del self.__data[index]
        else:
            raise IndexError("index outside array bounds")
        
    def sort(self):
        self.__data.sort()
        


def main():
    c1 = Cars("ABC", 222)
    c2 = Cars("ABC", 151)
    c3 = Cars("DEF", 121)
    cars = ListCars([c1, c2, c3])
    print(cars.data)
    cars.sort()
    print(cars.data)
    print(cars.data[0])

if __name__ == "__main__":
    main()


'''
[222, 151, 121]
[121, 151, 222]
121
'''