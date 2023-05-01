'''
    Realize a leitura dos arquivos 'funcionario e dependente'
    O arquivo representa os metadados de uma tabela, contendo os atributos.
    As seguintes operações devem ser realizadas:

    1. Montar um dicionário em que a chave é o nome da tabela e os valores são uma lista de tuplas que contém 
        os metadados de cada atributo.
    2. Possibilitar que o usuário possa escolher listar as tabelas lidas, os atributos de cada tabela e suas 
        chaves primárias.
'''

import os

addressDir = "/home/wesley/Área de Trabalho/python/exercises/arquivos_exercise1"

# Realiza a leitura do nome de um arquivo.
# Separa o nome e o tipo do arquivo.
# Retorna o nome do arquivo, que é o nome de uma tabela.
# Não necessário no linux, pois o arquivo texto não tem tipo explícito.
def read_name_file(nameFile):
    return nameFile.split(".")[0]

# Realiza a leitura de todas as linhas do arquivo.
# Ao abrir o arquivo, separa em linhas.
# Cada linha é separada pelo char '\t'.
# Retorna uma lista de tuplas, que são os metadados das colunas de uma tabela.
def read_lines_file(nameFile):
    file = open(os.path.join(addressDir, nameFile), "rt").read()
    file = file.split("\n")
    attributes = []
    for line in file:
        if line:
            line = line.split("\t")
            attributes.append((line[0], line[1], line[2]))
    return attributes

# Realiza a leitura dos arquivos.
# Recebe o endereço do diretório e o dicionário que conterá as tabelas e identificadores.
def read_files(addressDir, tables):
    for nameFile in os.listdir(addressDir):
        tables[nameFile] = read_lines_file(nameFile)

# Imprime os dados de uma tabela
# Cada table é uma lista de tuplas
def print_table(tables, name):
    print("Tabela '{}':".format(name))
    attibutes = tables[name]
    for col in attibutes:
        print("\t\t{}\t{}\t{}".format(col[0], col[1], col[2]))

def print_keys_tables(tables):
    for key, value in tables.items():
        print("\t{} --> {}".format(key, value[0][0]))

# Manipula as interações com o usuário.
def input_user(tables):
    print("Endereço do diretório atual: '{}'".format(addressDir))
    while True:
        print("\nSelecione uma das opções abaixo:")
        option = input("1 - Listar as tabelas lidas;\n2 - Imprimir descritivo da tabela;\n3 - Listar pares tabela-chave\n4 - Sair\n:")
        if option == '1':
            for name in tables.keys():
                print("\t{}".format(name))
        elif option == '2':
            option = input("Nome da tabela: ")
            if option in tables.keys():
                print_table(tables, option)
            else:
                print("* Essa tabela não existe *")
        elif option == '3':
            print_keys_tables(tables)
        elif option == '4':
            break
        else:
            print("* Opção inválida *")
    print("* Programa encerrado *")

# Função main
def main():
    tables = {}
    read_files(addressDir, tables)
    input_user(tables)

if __name__ == "__main__":
    main()