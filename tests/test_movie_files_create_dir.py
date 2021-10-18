
from mlutils.movie_files_create_dir import *


def test_mfcd():
    
    assert create_dir('/mnt/c/Users/Diego/Downloads/path') == None
    assert move_files('/mnt/c/Users/Diego/Downloads/path', '/mnt/c/Users/Diego/Downloads/path2') == None
    
test_mfcd()