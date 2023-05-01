class FileIterable:

    def __init__(self, fileName):
        self.__file = open(fileName, 'r')
    
    def __iter__(self):
        return self

    def __next__(self) -> str:
        line = self.__file.readline()
        if not line:
            self.__file.close()
            raise StopIteration
        return line
    

def main():
    frutas = FileIterable('exercise12/frutas')

    # Não carrega todo o arquivo na memória, somente carrega uma linha por vez
    for fruta in frutas:
        print(fruta, end="")

if __name__ == "__main__":
    main()