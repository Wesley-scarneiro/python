# NameError
def nameError():
    try:
        print(x)
    except NameError as e:
        print("Error: ",e)

# TypeError
def typeError(index: int):
    fruits = ["apple", "pineapple", "strawberry", "orange"]
    try:
        print("Selected fruit: ", fruits[index])
    except TypeError as e:
        print("Error: ", e)

# KeyError
def keyError(key: str):
    fruits = {"apple":"maça", "pineapple":"abacaxi", "strawberry":"morango", "orange":"laranja"}
    try:
        print(f"Translation: {key} --> {fruits[key]}")
    except KeyError as e:
        print("Error: ", e)

# IndexError
def indexError(index: int):
    fruits = ["apple", "pineapple", "strawberry", "orange"]
    try:
        print("Selected fruit: ", fruits[index])
    except IndexError as e:
        print("Error: ", e)

# ZeroDivisionError
def zeroDivisionError(x: int, y: int):
    try:
        print(f"{x}/{y} = {x/y}")
    except ZeroDivisionError as e:
        print("Error: ", e)

# AttributeError
def attributeError():
    class Car:
        def __init__(self, name):
            self.name = name
    try:
        car = Car("HB20")
        print(car.color)
    except AttributeError as e:
        print("Error: ", e)

def main():
    nameError()
    typeError(10.6)
    typeError("purposeful")
    keyError(4)
    keyError("apples")
    indexError(4)
    zeroDivisionError(5, 0)
    attributeError()
if __name__ == "__main__":
    main()


'''
Error:  name 'x' is not defined
Error:  list indices must be integers or slices, not float
Error:  list indices must be integers or slices, not str
Error:  4
Error:  'apples'
Error:  list index out of range
Error:  division by zero
Error:  'Car' object has no attribute 'color'
'''