from collections import namedtuple

People = namedtuple('People', ['name', 'gender', 'age'])
maria = People('Maria', 'female', '25')
print(maria)
print(maria[2])

'''
People(name='Maria', gender='female', age='25')
25
'''