import shutil
import os


def move_files(source_dir: str, dest_dir: str):
    """
    moves the files from source_dir to dest_dir.
    :param source_dir:  
    :type: Str
    :param dest_dir:
    :type: Str
    :return:  
    :rtype:

    """
    create_dir(dest_dir)

    for file in os.listdir(source_dir):
        shutil.copy(source_dir + file, dest_dir)
        


#TODO: Fazer a função ficar invariante a SO.
def create_dir(save_dir: str): 
    """
    Creates directoy if doesn't exist.
    :param path
    :type: str
    :return: 
    :rtype: str  
   
    """

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)