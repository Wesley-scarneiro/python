import os
import zipfile
import sys

# Caminho do arquivo
path = "/home/wesley/Área de Trabalho/python/projetos/dados.zip"

# A função recebe o caminho do arquivo.
# Se o caminho não existe, encerra.
# Se o caminho existe, realiza a extração.
def main(path):
    if not os.path.exists(path):
        print("Arquivo '{}' não existe.".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos extraídos.")

if __name__ == "__main__":
    main(path)