import shutil
import os
from pathlib import Path


def create_dir(save_dir: str):
    """
    Creates directoy if doesn't exist.
    
    :param save_dir: path directory where the files will be saved
    :type: str
    :raise exception: file already exists 
   
    """

    try:
        Path(save_dir).mkdir(parents=True, exist_ok=False)

    except:
        print("Folder already exists")

    else:
        print("Folder was created")


def move_files(source_dir: str, dest_dir: str):
    """
    Moves the files from source_dir to dest_dir.
    
    :param source_dir: the source directory where are the files initially located  
    :type: Str
    :param dest_dir: the destiny directory where the files will be located
    :type: Str
    :raise exception: An error occured during file's creation

    """

    try:
        create_dir(dest_dir)
        source_dir_path = Path(source_dir)
        for file in os.listdir(source_dir):
            shutil.copy(str(source_dir_path / file), dest_dir)

    except Exception:
        print("An error occured while moving file")

    else:
        print("files moved successfully")
