from codes.shoppingList import ShoppingList
from codes.product import Product
from typing import List
import random

def openFile(file: str) -> str:
    try:
        with open(file, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(e)

def dataProcessing(data: str) -> List[Product]:
    record = []
    for line in data.split("\n"):
        line = line.split("\t")
        record.append(line)
    products = []
    for product in record:
        product = Product(int(product[0]), product[1], float(product[2]), float(product[3]))
        products.append(product)
    return products

def buyProducts(shopList: ShoppingList, products : List[Product]) -> None:
    try:
        for i in range(0, 50):
            shopList.add_item(products[random.randint(0, len(products)-1)])
        shopList.printList()
    except TypeError as e:
        print("Error: ", e)

def removeProducts(shopList: ShoppingList, products : List[Product]) -> None:
    try:
        for i in range(0, 10):
            shopList.remove_item(products[random.randint(0, len(products)-1)])
        shopList.printList()
    except TypeError as e:
        print("Error: ", e)

def main():
    shopping = ShoppingList("Month shopping")
    data = openFile("/home/wesley/Área de Trabalho/python/exercises/exercise8/products.txt")
    products = dataProcessing(data)
    buyProducts(shopping, products)
    removeProducts(shopping, products)

if __name__ == "__main__":
    main()

'''
Name list: Month shopping
Total products: 50
Products: 
        Shampoo Lava Tudo - R$ 7.99 * (7) = RS 55.93
        Refrigerante Cola - R$ 8.3 * (2) = RS 16.6
        Aveia em flocos - R$ 3.99 * (4) = RS 15.96
        Arroz Anãozinho - R$ 14.5 * (3) = RS 43.5
        Sabonete Bãozaum - R$ 1.99 * (5) = RS 9.95
        Feijão Saborbão - R$ 11.99 * (6) = RS 71.94
        Papel Higiênico - R$ 2.49 * (3) = RS 7.470000000000001
        Feijão Dubom - R$ 8.49 * (3) = RS 25.47
        Feijão Maranhão - R$ 6.99 * (4) = RS 27.96
        Macarrão Parafuso - R$ 4.99 * (6) = RS 29.94
        Miojo Caipirinha - R$ 0.99 * (2) = RS 1.98
        Arroz Solimões - R$ 15.99 * (2) = RS 31.98
        Arroz Salvação - R$ 19.99 * (2) = RS 39.98
        Leite Vida Curta - R$ 4.49 * (1) = RS 4.49
Total price: R$ 383.15000000000003

Name list: Month shopping
Total products: 34
Products: 
        Aveia em flocos - R$ 3.99 * (4) = RS 15.96
        Arroz Anãozinho - R$ 14.5 * (3) = RS 43.5
        Sabonete Bãozaum - R$ 1.99 * (5) = RS 9.95
        Feijão Saborbão - R$ 11.99 * (6) = RS 71.94
        Feijão Maranhão - R$ 6.99 * (4) = RS 27.96
        Macarrão Parafuso - R$ 4.99 * (6) = RS 29.94
        Miojo Caipirinha - R$ 0.99 * (2) = RS 1.98
        Arroz Solimões - R$ 15.99 * (2) = RS 31.98
        Arroz Salvação - R$ 19.99 * (2) = RS 39.98
Total price: R$ 273.19
'''