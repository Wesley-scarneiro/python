numbers = [i for i in range(10)]
print(numbers)

numbersDouble = [i*2 for i in range(10)]
print(numbersDouble)

even = [i for i in range(10) if i%2 == 0]
print(even)

odd = [i for i in range(1, 10, 2)]
print(odd)

tuples = [(i, j) for i in range(3) for j in range(3)]
print(tuples)

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
'''