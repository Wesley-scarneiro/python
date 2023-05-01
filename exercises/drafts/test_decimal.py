from decimal import Decimal, getcontext, FloatOperation

# float com precisão aproximada
a = 0.1 + 0.1 + 0.1 - 0.3
print("float --> ", a)

# float com precisão mais exata
b = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print("Decimal -->", b)

# Decimal() também aceita algumas constantes...
print(Decimal('NaN'))
print(Decimal('Infinity'))

# Comparações entre float e Decimal
print(f"Decimal(0.1) < 0.19 = {Decimal(0.1) < 0.19}")

# Impedindo comparações entre float e Decimal, através do lançamento de exceções
try:
    c = getcontext()
    c.traps[FloatOperation] = True
    print(f"Decimal(0.1) < 0.19 = {Decimal(0.1) < 0.19}")
except FloatOperation as e:
    print("Error: ", e)

'''
float -->  5.551115123125783e-17
Decimal --> 0.0
NaN
Infinity
Decimal(0.1) < 0.19 = True
Error:  [<class 'decimal.FloatOperation'>]
'''