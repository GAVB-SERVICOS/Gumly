
from mlutils.movie_files_create_dir import *


def test_mfcd():
    
    
    resultado_cd = create_dir('/mnt/c/Users/Diego/Downloads/path')
    resultado_mf = move_files('/mnt/c/Users/Diego/Downloads/path', '/mnt/c/Users/Diego/Downloads/path2')
    
    assert create_dir('/mnt/c/Users/Diego/Downloads/path') == 1
    assert move_files('/mnt/c/Users/Diego/Downloads/path', '/mnt/c/Users/Diego/Downloads/path2') == 1
    
    return resultado_mf, resultado_cd

test_mfcd()