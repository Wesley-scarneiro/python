def methodOne(x: int | float, y: int | float):
    try:
        print(f"{x}/{y} = {methodTwo(x, y)}")
    except ZeroDivisionError as e:
        print("Error: ", e)
    except TypeError as e:
        print("Error: ", e)

def methodTwo(x: int | float, y: int | float) -> float:
    try:
        return x/y
    except ZeroDivisionError:
        raise
    except TypeError:
        raise

def exceptionCreation():
    class VowelError(Exception):
        def __init__(self, message: str):
            super().__init__(message)
            self.message = message
    
    def vowels(letter: str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        if letter in vowels:
            print(f"Letter {letter} is a vowel")
        else:
            raise VowelError("the letter given is not a vowel")
    
    try:
        vowels("b")
    except VowelError as e:
        print("Error: ", e)

def exceptionWithFinally(string: str):
    print("Function start")
    try:
        print(f"\tlength({string}) = {len(string)}")
    except TypeError as e:
        print("\tError: ", e)
    finally:
        print("Function end")
    
def main():
    methodOne(10, 0)
    methodOne(10, "a")
    exceptionCreation()
    exceptionWithFinally(100)

if __name__ == "__main__":
    main()

'''
Error:  division by zero
Error:  unsupported operand type(s) for /: 'int' and 'str'
Error:  the letter given is not a vowel
Function start
        Error:  object of type 'int' has no len()
Function end
'''