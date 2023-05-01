import os

# Divide uma string e retorna o primeiro elemento.
def extract_name(name):
    return name.split(".")[0]

# Faz o join entre o nome do arquivo e o diretório onde ele se encontra.
# Realiza a leitura do arquivo e divide os dados em linhas.
# Retorna uma lista de strings, em que cada elemento é o conteúdo de uma linha do arquivo lido.
def read_lines(filename):
    _file = open(os.path.join("/home/wesley/Área de Trabalho/python/projetos/data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

# Metada é um dicionário para guardar informações sobre cada coluna do arquivo.
# read_lines retorna as linhas do arquivo.
# A cada iteração uma linha do arquivo é copiada para column, que a divide em elementos através do '\t'.
# Os elementos são separados e guardados em tuplas em metada.
def read_metadata(filename):
    metada = []
    for column in read_lines(filename):
        if column:
            values = column.split("\t")
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metada.append((nome, tipo, desc))
    return metada

# 'meta' é o dificonário, que guarda o conjunto de atributos de cada tabela.
#  Após obter o conjunto de atributos de uma tabela, obtem-se o identificador.
# O identificador é guardado em 'keys', sendo a chave para o nome de uma tabela.
# No segundo for, 'val' retorna tuplas que são guardadas em 'col'.
# 'col' acessa o primeiro elemento, que é o atributo identificador da coluna (chave primária).
# Se 'col[0]' está em 'keys' como chave, então é verificado se não estamos nos referindo a tabela que o contém
# como chave primária. Se for outra tabela, então imprime a relação.
def main():
    meta = {} 
    keys = {}

    for meta_data_file in os.listdir("/home/wesley/Área de Trabalho/python/projetos/data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print("Entidade {} -> {}".format(key, col[0]))

if __name__ == "__main__":
    main()