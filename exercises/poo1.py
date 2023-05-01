class Account:

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    '''
        outro modo possível para um get:

        def _get_name(self):
            return self.__name
        
        name = property(_get_name)
    '''

    @name.setter
    def name(self, name):
        self.__name = name

class A:
    def run(self):
        print("Classe A")

class B:
    def run(self):
        print("Classe B")

class C(B, A): # Herençã multipla.
    pass


c = C()
c.run()
a = A()
print(isinstance(a, C))