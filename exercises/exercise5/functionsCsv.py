import os
from typing import List
import pandas as pd

# Return a list that contains the names of files .csv or 'None' if the path does not exist
def open_directory(path:str, kind: str) -> List[str]:
    try:
        files = os.listdir(path)
        files = filter_files(files, kind)
        return files
    except FileNotFoundError as e:
        print(f"\tThe path '{e.filename}' does not exist")
        return None
    
# Filters the file list according to the specified type or 'None'
def filter_files(files: List[str], kind: str) -> List[str]:
    newFiles = []
    for file in files:
        if kind in file:
            newFiles.append(file)
    if newFiles:
        return newFiles
    else:
        print(f"\tDoes not exist files of the type '{kind}' to filter")
        return None

# Shows the files and their index
def show_files(files: List[str]):
    if not files is None:
        _str = ""
        for index, file in enumerate(files):
            _str += "\t" + str(index) + " - " + file + "\n"
        print(_str)
    else:
        raise ValueError("\tDoes not exist files to show")

# Returns the path of the folder if it not exist or throws an exception
def create_folder(pathDir: str, nameFolder: str) -> str:
    newDir = os.path.join(pathDir, nameFolder)
    try:
        os.makedirs(newDir)
        return newDir
    except FileExistsError as e:
        print(f"\tThe directory '{e.filename}' already exist and not can create")
        return None
    except PermissionError as e:
        print(f"\tNo permission to create directory '{e.filename}'")
        return None

def convertall_toexcel(pathDir: str, nameFolder: str,  files: List[str]):
    newDir = create_folder(pathDir, nameFolder)
    try:
        for file in files:
            dataframe = pd.read_csv(os.path.join(pathDir, file), sep=";")
            dataframe.to_excel(os.path.join(newDir, file.replace(".csv", ".xlsx")), index=False)
    except Exception:
        print("\tError during conversion")

def convertone_toexcel(pathCsv: str, pathFolder: str, file: str):
    try:
        dataframe = pd.read_csv(os.path.join(pathCsv, file), sep=";")
        dataframe.to_excel(os.path.join(pathFolder, file.replace(".csv", ".xlsx")), index=False)
    except Exception:
        print("\tError during conversion")