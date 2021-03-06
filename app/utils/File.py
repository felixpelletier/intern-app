import pandas as pd
import os
from shutil import rmtree
from glob import glob
from pathlib import Path

def get_uploads_files(dir_name=r'./uploads'):
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        if not os.listdir(dir_name):
            print("Directory is empty")
            return []
        else:
            print("Directory is not empty")
            return os.listdir(dir_name)
    else:
        print("Given directory doesn't exist")
        return []


def purge_file(dir_name=r'./uploads'):
    if get_uploads_files(dir_name) != []:
        for file in get_uploads_files(dir_name):
            os.remove(os.path.join(dir_name, file))


def validate_file_epow(file):
    col30 = set(['Bus kV', 'Sym Amps'])
    col1 = set(["Bus kV","Sym Amps","X/R Ratio","Mult Factor","Asym Amps","Equip Type","Duty Amps"])
    try:
        df = pd.DataFrame(pd.read_csv(file, skiprows=1, index_col=0))
    except:
        try:
            df = pd.DataFrame(pd.read_excel(file, skiprows=5, index_col=0, engine='openpyxl'))
        except openpyxl.utils.exceptions.InvalidFileException as notXL:
            return -1

    if col1.issubset(df.columns.to_list()) or col30.issubset(df.columns.to_list()):
        return 0
    else:
        return -1


def full_paths(upload_dir):
    return glob(os.path.join(upload_dir, "*"))

def create_dir_if_dont_exist(dir_name):
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    return dir_name

