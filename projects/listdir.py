import os

path = "/home/wesley/Área de Trabalho/python/projetos/data/meta-data"

# Usa o módulo 'os' para listar os diretórios de uma pasta.
def listDir(path):
    if not os.path.exists(path):
        print("Caminho do diretório '{}' não existe.".format(path))
    else:
        for file in os.listdir(path):
            
            print(file)

def extract_name_file(fileName):
    return fileName.split(".")[0]

# Abre e lê o arquivo linha por linha, separando suas partes pelo caractere '\t'.
# open() retorna um objeto de arquivo aberto.
# meta_data[] recebe uma lista de tuplas.
def read_meta_data(path):
    data = open(path, "rt")
    meta_data = []

    for line in data:
        line_data = line.split("\t")
        meta_data.append((line_data[0], line_data[1], line_data[2]))
    
    data.close()
    return meta_data


if __name__ == "__main__":
    listDir(path)


