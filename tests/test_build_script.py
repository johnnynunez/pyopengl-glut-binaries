"""The GLE build script's files appear whole or not at all."""

import importlib.util
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), 'tools', 'buildgledll.py')


@pytest.fixture(scope='module')
def script():
    pytest.importorskip('requests')
    spec = importlib.util.spec_from_file_location('buildgledll', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_a_finished_write_takes_the_place_of_the_file(script, tmp_path):
    target = tmp_path / 'gle.tar.gz'
    target.write_bytes(b'old')
    with script.whole(str(target)) as partial, open(partial, 'wb') as handle:
        handle.write(b'new')
    assert target.read_bytes() == b'new'
    assert os.listdir(tmp_path) == ['gle.tar.gz']


def test_a_write_cut_short_leaves_the_file_and_nothing_beside_it(script, tmp_path):
    target = tmp_path / 'gle.tar.gz'
    target.write_bytes(b'old')
    with pytest.raises(OSError), script.whole(str(target)) as partial:
        with open(partial, 'wb') as handle:
            handle.write(b'ne')
        raise OSError('disk full')
    assert target.read_bytes() == b'old'
    assert os.listdir(tmp_path) == ['gle.tar.gz']


def test_a_copy_cut_short_leaves_nothing_beside_the_target(script, tmp_path):
    target = tmp_path / 'gle.dll'
    with pytest.raises(OSError):
        script.copy_whole(str(tmp_path / 'missing.dll'), str(target))
    assert os.listdir(tmp_path) == []
