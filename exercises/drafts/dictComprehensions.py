numbers = [1,2,3,5]
names = ['one', 'two', 'three', 'four', 'five']
NumbersDict = {key:value for key, value in zip(numbers, names)}
print(NumbersDict)

# zip() itera simultaneamente dois iteráveis
for number, name in zip(numbers, names):
    print(f"{number}:{name}")

'''
{1: 'one', 2: 'two', 3: 'three', 5: 'four'}
1:one
2:two
3:three
5:four
'''