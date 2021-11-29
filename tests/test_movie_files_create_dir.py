from mlutils.move_files_create_dir import *
import tempfile
from pathlib import Path


def test_move_file():
    dirpath = Path(tempfile.mkdtemp())
    dest_dir = Path(tempfile.mkdtemp())

    dirpath.mkdir(parents=True, exist_ok=True)
    dest_dir.mkdir(parents=True, exist_ok=True)
    test_file = dirpath / "test.txt"
    with open(test_file, "w") as fd:
        fd.write("Testando para ver se move")
    move_files(str(dirpath), str(dest_dir))
    # import pdb
    # pdb.set_trace()
    assert (dest_dir / "test.txt").is_file()


def test_create_file():
    dirpath = Path(tempfile.mkdtemp())
    dirpath.mkdir(parents=True, exist_ok=True)
    create_dir(str(dirpath))
    assert dirpath.is_dir
