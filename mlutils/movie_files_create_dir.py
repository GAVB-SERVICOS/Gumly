import shutil
import os
from pathlib import Path


def move_files(source_dir: str, dest_dir: str):
    """
    moves the files from source_dir to dest_dir.
    
    :param source_dir: the source directory where are the files initially located  
    :type: Str
    :param dest_dir: the destiny directory where the files will be located
    :type: Str
        

    """
    create_dir(dest_dir)
    source_dir_path = Path(source_dir)
    for file in os.listdir(source_dir):
        shutil.copy(str(source_dir_path / file), dest_dir)

def create_dir(save_dir: str):
    """
    Creates directoy if doesn't exist.
    :param save_dir: path directory where the files will be save
    :type: str
    :raise FileExistsError: file already exists 
   
    """
    try:
        Path(save_dir).mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists")
    else:
        print("Folder was created and file moved")
