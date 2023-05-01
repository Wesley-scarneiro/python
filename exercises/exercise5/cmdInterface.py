import functionsCsv as fc
from typing import List

def list_all_csv(filesList):
    fc.show_files(filesList)

def convert_all_csv(pathDir, nameFolder, filesList):
    fc.convertall_toexcel(pathDir, nameFolder, filesList)

def convert_one_csv(pathDir, nameFolder, filesList):
    pathFolder = fc.create_folder(pathDir, nameFolder)
    while True:
        try:
            list_all_csv(filesList)
            index = input("    file index or 'exit': ")
            if index == "exit":
                break
            elif int(index) < 0 or int(index) > len(filesList)-1:
                print("    Invalid index")
            else:
                print("    processing...")
                fc.convertone_toexcel(pathDir, pathFolder, filesList[int(index)])
                filesList.pop(int(index))
                print("    fineshed")
                if not filesList:
                    break
        except ValueError:
            print("    Invalid index")

def options() -> str:
    _str = '''    exit - To quit
    1 - List all .csv files read
    2 - Convert all read .csv files
    3 - Convert a read .csv files'''
    print(_str)

def input_directory() -> List[str]:
    filesList = None
    while(filesList is None):
        pathCsv = input("Directory path: ")
        filesList = fc.open_directory(pathCsv, ".csv")
    return (pathCsv, filesList)

def start():
    inputReturn = input_directory()
    pathDir = inputReturn[0]
    filesList = inputReturn[1]
    nameFolder = "xlsx"
    while True:
        options()
        option = input("    :")
        if option == "1":
            list_all_csv(filesList)
        elif option == "2":
            print("\tprocessing...")
            close = convert_all_csv(pathDir, nameFolder, filesList)
            print("\tfinished")
            break
        elif option == "3":
            close = convert_one_csv(pathDir, nameFolder, filesList)
            break
        elif option == "exit":
            break
        else:
            print("\tInvalid option\n")
    print("Closed program")

def main():
    start()

if __name__ == "__main__":
    main()