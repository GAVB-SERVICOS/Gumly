from gumly.files import *
import tempfile
from pathlib import Path
import pytest
import shutil


@pytest.fixture()
def get_tmp_dir():
    tmp_dir = Path(tempfile.mkdtemp())
    tmp_dir.mkdir(parents=True, exist_ok=True)
    yield tmp_dir
    shutil.rmtree(str(tmp_dir))


src_tmp_dir = get_tmp_dir
dst_tmp_dir = get_tmp_dir


def test_move_file(src_tmp_dir, dst_tmp_dir):
    test_file = src_tmp_dir / "test.txt"
    with open(test_file, "w") as fd:
        fd.write("Testando para ver se move")
    assert not (dst_tmp_dir / "test.txt").is_file()
    move_files(str(src_tmp_dir), str(dst_tmp_dir))
    assert (dst_tmp_dir / "test.txt").is_file()


def test_create_non_existing_dir(get_tmp_dir):
    dirpath = get_tmp_dir / 'test'
    assert not dirpath.is_dir()
    create_dir(str(dirpath))
    assert dirpath.is_dir()


def test_create_existing_dir(get_tmp_dir):
    assert get_tmp_dir.is_dir()
    create_dir(str(get_tmp_dir))
    assert get_tmp_dir.is_dir()
