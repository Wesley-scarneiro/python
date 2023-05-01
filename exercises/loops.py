# Lista
names = ["Ana", "Matheus", "Aline", "Pedro", "Maria", "João"]

# Imprimindo com while
print("Imprimindo com while")
i = 0
while i < len(names):
    print(names[i] + " ")
    i += 1

# Imprimindo com for
print("\nImprimindo com for")
for name in names:
    print(name)

# Usando for e range()
# Range é um objeto do tipo iterável, que nesse exemplo retorna inteiros de 0 a 5.
for i in range(5):
    print(i)

# Retornando a lista enumerada.
for i, name in enumerate(names):
    print(i, name)