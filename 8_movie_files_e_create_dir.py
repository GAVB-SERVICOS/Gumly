import shutil
import os
from pathlib import Path


def move_files(source_dir: str, dest_dir: str):
    """
    moves the files from source_dir to dest_dir.
    
    :param source_dir:  
    :type: Str
    :param dest_dir:
    :type: Str
    :return:    
    :rtype: str

    """
    create_dir(dest_dir)

    for file in os.listdir(source_dir):
        shutil.copy(source_dir + file, dest_dir)
        



def create_dir(save_dir: str): 
    """
    Creates directoy if doesn't exist.
    :param path
    :type: str
    :raise FileExistsError: File already exists
    :return: 
    :rtype: str  
   
    """
    try:
        Path(save_dir).mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists")
    else:
        print("Folder was created")