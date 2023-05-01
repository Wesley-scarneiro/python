class A:
    
    def __init__(self, name):
        self.name = name
    
    # informal representation
    def __str__(self):
        return self.name

class B:

    def __init__(self, name):
        self.name = name
    
    # formal representation
    def __repr__(self):
        return self.name


def generator(_class):
    _list = []
    for i in range(5):
        _list.append(_class(f'{_class.__name__}{i}'))
    return _list

def main():
    classA = generator(A)
    classB = generator(B)
    print("With '__str__': ", classA)
    print("With '__repr__' B: ", classB)

if __name__ == "__main__":
    main()

'''
With '__str__':  [<__main__.A object at 0x7faf9b25bd60>, <__main__.A object at 0x7faf9b25ba60>, <__main__.A object at 0x7faf9b25ba00>, <__main__.A object at 0x7faf9b25b9a0>, <__main__.A object at 0x7faf9b25b940>]
With '__repr__' B:  [B0, B1, B2, B3, B4]
'''