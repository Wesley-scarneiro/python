from datetime import *

# Somente data
print(date(2023, 4, 20))

# Somente hora
print(datetime.now().strftime('%H:%M:%S'))

# Data e hora
print(datetime.now())
print(datetime.today())

# Como calcular uma idade com base na data atual?
dateBirth = datetime.strptime('06/04/1995', '%d/%m/%Y')
dateToday = datetime.today()
age = int(((dateToday - dateBirth).days)/365)
print(f"Age: {age} years")

'''
2023-04-20
09:06:05
2023-04-21 09:06:05.977696
2023-04-21 09:06:05.977735
Age: 28 years
'''

