def greater(FixedValue):
    def _greater(value):
        return value > FixedValue
    return _greater

greater100 = greater(100)
print(greater100(99))
print(greater100(101))