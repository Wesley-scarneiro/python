def sum(x, y):
    return x + y

print("x + y = {}".format(sum(10, 30)))

def exp(x, y):
    return x ** y

print("x^y = {}".format(exp(2, 10)))

def calcSalary(salary, tax = 27.0):

    salaryLiquid = salary - (salary * (tax/100))
    print("Salary liquid = R$ {}\nTax = {}%".format(salaryLiquid, tax))


calcSalary(3500)
calcSalary(3500, 20)
calcSalary(salary=3500, tax=45)
calcSalary(3500)

def biggerNumber(x, y, z):

    bigger = x
    if (bigger < y):
        bigger = y
    if (bigger < z):
        bigger = z
    print("The bigger is '{}'".format(bigger))

biggerNumber(14,2,3) # Passando manualmente cada parâmetro
numbers = [14, 2, 3]
biggerNumber(*numbers) # Usando parameters packing

# Unpacking parameters - positional
def printPeople(*args):
    print("1º - {}\n2º - {}\nOthers - {}".format(args[0], args[1], args[2:]))

printPeople("Wesley", "Zailda", "Elias", "Luana", "Melissa", "Erick")

# Unpacking parameters - nominated
def printValues(**kwargs):
    print(kwargs)

printValues(sp="São Paulo", rj="Rio de Janeiro", rs="Rio grande do Sul")
