import shutil
import os
from pathlib import Path
from mlutils.movie_files_create_dir import *


def test_mfcd():
    
    
    resultado_mf = move_files('/mnt/c/Users/Diego/Downloads/path', '/mnt/c/Users/Diego/Downloads/path2')
    resultado_cd = create_dir('/mnt/c/Users/Diego/Downloads/path')

    return resultado_mf, resultado_cd

test_mfcd()