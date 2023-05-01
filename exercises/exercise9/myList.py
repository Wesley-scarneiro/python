from collections import UserList

class MyList(UserList):

    def __init__(self, initlist=None):
        super().__init__()
        if initlist:
            for item in initlist:
                self.append(item)

    # call MyList[index] = value
    def __setitem__(self, index, value):
        if isinstance(value, float):
            super().__setitem__(index, value)
        else:
            raise TypeError(f"This list not support the type '{type(value)}'")
    
    def append(self, value):
        if isinstance(value, float):
            super().append(value)
        else:
            raise TypeError(f"This list not support the type {type(value)}")
        

def main():
    try:
        lst = MyList()
        lst.append(7.88)
        print(lst)
    except TypeError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()

'''
Error:  This list not support the type '<class 'str'>'
Error:  This list not support the type '<class 'bool'>'
[7.88]
'''