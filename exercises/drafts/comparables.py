'''
object.__lt__(self, other) | x < y
object.__le__(self, other) | x <= y
object.__ne__(self, other) | x != y
object.__gt__(self, other) | x > y
object.__ge__(self, other) | x >= y
'''

import random

class Person:

    def __init__(self, id):
        self.name = "person-" + str(id)
        self.id = id
    
    def __repr__(self):
        return self.name

    # allows comparison by equality
    def __eq__(self, other):
        return self.id == other.id
    
    # to sorting
    def __lt__(self, other):
        return self.id < other.id
    
def generator(_class):
    _list = []
    for i in range(5):
        _list.append(_class(random.randint(100,200)))
    _list.append(_class(_list[0].id))
    return _list

def main():
    people = generator(Person)
    print(people)
    print(f"{people[0]} == {people[-1]} -> {people[0]==people[-1]}")
    people.sort()
    print(people)


if __name__ == "__main__":
    main()