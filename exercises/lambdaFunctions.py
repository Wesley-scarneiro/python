add = lambda x, y: x +y
print(add(10,20))

numbers = [1, 5, 3, 8, 15, 16, 23, 22, 10, 2]
numbersEven = list(filter(lambda x: x % 2 == 0, numbers))
numbersOdd = list(filter(lambda x: x % 2 == 1, numbers))
print(numbersEven)
print(numbersOdd)

divisivel = lambda x, y: x % y == 0
print(divisivel(4,2))
print(divisivel(10,3))
print(divisivel(10,5))