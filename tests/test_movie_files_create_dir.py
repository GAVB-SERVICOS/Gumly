
from mlutils.movie_files_create_dir import *


def test_mfcd():
    assert create_dir('/mnt/c/Users/Diego/Downloads/path') == None
    
test_mfcd()