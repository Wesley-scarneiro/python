#################################
# Decorators através de funções #
#################################

# Decorator
def fullName(function):
    def lastName(first, last):
        print(function(f"{first} {last}"))
    return lastName

# Uma função simples com decorator
@fullName
def firstName(name):
    return name

print("With function: ", end="")
firstName('Alan', 'Turing')

#################################
# Decorators através de classes #
#################################
class FullName:

    def __init__(self, function):
        self.function = function

    def __call__(self, first, last):
        print(self.function(f"{first} {last}"))


@FullName
def firstName2(name):
    return name

print("With class: ", end="")
firstName2('John', 'Neumann')

'''
With function: Alan Turing
With class: John Neumann
'''