'''
    Escreva duas funções diferentes que consigam encontrar todos os números primos entre um intervalo [x, y].
    A primeira função deve iterar no intervalo [2, x) para verificar se x é primo.
    A segunda função deve iterar no intervalo [2, raizQuadrada(x)+1], para verificar se x é primo.
    Se o intervalo fornecido for decrescente, a função deve torná-lo crescente.
    A função deve retornar uma lista que contém os números primos encontrados.
    Calcule a diferença de tempos entre as funções.
'''

import math
import time

# Testa a primalidade de um número x, realizando o teste de divisão de 2 até x-1.
def primos1(x, y):
    if y < x:
        temp = x
        x = y
        y = temp
    primos = []
    for i in range(x, y+1):         # Itera de i = x enquanto x < y + 1
        label = False if (i == 0 or i == 1) else True
        for j in range(2, i):       # Itera de j = 2 enquanto j < x
            if i % j == 0:
                label = False
                break
        if label:
            primos.append(i)
    return primos

# Testa a primalidade de um número x, realizando o teste de divisão de 2 até a sqrt(x).
# Se um número x não é divisível pelos números menores do que a sua raiz quadrada, então ele é provavelmente primo.
def primos2(x, y):
    if y < x:
        temp = x
        x = y
        y = temp
    primos = []
    for i in range(x, y+1):         # Itera de i = x enquanto x < y + 1
        if isPrimo(i):
            primos.append(i)
    return primos

def isPrimo(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# calcula o tempo
def calcularTempo(function, x, y):
    start = time.time()
    function(x, y)
    end = time.time()
    return end - start

if __name__ == "__main__":
    print("Tempo para primos1(0, 100000): {}s".format(calcularTempo(primos1, 0, 100000)))
    print("Tempo para primos2(0, 100000): {}s".format(calcularTempo(primos2, 0, 100000)))

