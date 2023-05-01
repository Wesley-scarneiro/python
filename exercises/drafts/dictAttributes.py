class A:

    def __init__(self):
        self.a = 0
        self.b = 0

    def method1(self):
        pass

print(A.__dict__)
a = A()
print(a.__dict__)
setattr(a, 'c', -1)
print(a.__dict__)
print(getattr(a, 'c'))
print(hasattr(a, 'a'))
print()


'''
Dicionário da classe: {'__module__': '__main__', '__init__': <function A.__init__ at 0x7f0ba1e6a4d0>, 'method1': <function A.method1 at 0x7f0ba1e6a560>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
Dicionário do objeto: {'a': 0, 'b': 0}
{'a': 0, 'b': 0, 'c': -1}
-1
True

'''