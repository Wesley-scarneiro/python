import abc
import math

class PlaneGeometry(abc.ABC):

    @abc.abstractclassmethod
    def perimeter(self) -> float:
        pass

    @abc.abstractclassmethod
    def area(self) -> float:
        pass

class Triangle(PlaneGeometry):

    def __init__(self, length: float):
        self.__length  = length
        self.__height = (math.sqrt(3)*length)/2

    def perimeter(self) -> float:
        return 3*self.__length
    
    def area(self) -> float:
        return (self.__length*self.__height)/2
    
class Square(PlaneGeometry):

    def __init__(self, length: float):
        self.__length  = length

    def perimeter(self) -> float:
        return 4*self.__length
    
    def area(self) -> float:
        return math.pow(self.__length, 2)

class Rectangle(PlaneGeometry):

    def __init__(self, width: float, height: float):
        self.__width  = width
        self.__height = height

    def perimeter(self) -> float:
        return 2*self.__width + 2*self.__height
    
    def area(self) -> float:
        return self.__width*self.__height

class Trapeze(PlaneGeometry):

    def __init__(self, smBase: float, lgBase: float, sides: float):
        self.__smBase = smBase
        self.__lgBase = lgBase
        self.__sides = sides
        self.__height = math.sqrt(math.pow(self.__sides, 2) + math.pow((self.__lgBase - self.__smBase)/2, 2))

    def perimeter(self) -> float:
        return self.__smBase + self.__lgBase + 2*self.__sides
    
    def area(self) -> float:
        return ((self.__smBase + self.__lgBase)*self.__height)/2