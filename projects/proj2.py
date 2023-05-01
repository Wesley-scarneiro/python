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

# Retorna o nome dos arquivos que estão no diretório específicado.
# Extrai o nome do arquivo, sem o formato, usando extract_name().
# Realiza a leitura do arquivo, repassando o nome dele para read_metada().
# A leitura do arquivo atual retorna uma lista de tuplas, que depois são impressas. 
def main():
    meta = {}
    for meta_data_file in os.listdir("/home/wesley/Área de Trabalho/python/projetos/data/meta-data"):
        table_name = extract_name(meta_data_file)
        meta[table_name] = read_metadata(meta_data_file)
    
    for key, val in meta.items():
        print("Entidades {}".format(key))
        print("Atributos: ")
        for col in val:
            print("\t{} : {}".format(col[1], col[0]))

if __name__ == "__main__":
    main()