import pytest
from directory import Directory
import logging

@pytest.fixture
def directory():
    instance = Directory(read_file='file_paths.txt', path='/shares/win7/Artbeats', sort='Alphanumeric')
    assert instance.read_file == 'file_paths.txt'
    assert instance.path == '/shares/win7/Artbeats'
    assert instance.sort == 'Alphanumeric'
    instance.get_items()
    return instance

@pytest.mark.parametrize('attribute, invalid_value, expected_exception', [
    ('read_file', 'file_paths.csv', ValueError),
    ('path', None, TypeError),
    ('sort', 'Recent', ValueError)
])
def test_directory_setters_invalid(directory, attribute, invalid_value, expected_exception):
    with pytest.raises(expected_exception) as excinfo:
        setattr(directory, attribute, invalid_value)
    assert f"Invalid {attribute.replace('_',' ')} attribute specified" in str(excinfo.value)

def test_directory_get_items_valid(directory):
    files = directory.get_items('Files')
    folders = directory.get_items('Folders')
    items = directory.get_items()
    assert '1920x1080-Artbeats-3-v2.mp4' in files and 'withMusic' not in files and \
            'withMusic' in folders and '1920x1080-Artbeats-3-v2.mp4' not in folders and \
            'withMusic' in items and '1920x1080-Artbeats-3-v2.mp4' in items

def test_directory_get_items_invalid(directory):
    with pytest.raises(ValueError) as excinfo:
        directory.get_items('Files/Folders')
    assert 'Invalid type parameter specified' in str(excinfo.value)

def test_directory_search_valid(directory):
    files = directory.get_items('Files', search_term='Mbps')
    folders = directory.get_items('Folders', search_term='short')
    items = directory.get_items(search_term='test')
    assert 'Artbeats1-5x2_1920x1080p30-50Mbps.mp4' in files and \
            'short_20s_versions' in folders and \
            'Artbeats_1a-copy-test.mp4' in items

def test_directory_search_invalid(directory):
    with pytest.raises(TypeError) as excinfo:
        directory.get_items(search_term=1920)
    assert 'Invalid search term parameter specified' in str(excinfo.value)

def test_directory_step_in_valid(directory):
    directory.step('In', subdirectory='withMusic')
    assert directory.path == '/shares/win7/Artbeats/withMusic' and \
            'Artbeats_3_25M_music_fast.mp4' in directory.get_items()

def test_directory_step_in_invalid(directory):
    with pytest.raises(ValueError) as excinfo:
        directory.step('In')
    assert 'Missing or invalid subdirectory parameter specified' in str(excinfo.value)

def test_directory_step_out(directory):
    directory.step('Out')
    assert directory.path == '/shares/win7'
    assert 'Artbeats' in directory.get_items()

def test_directory_sort_alphanumeric(directory):
    directory.sort = 'Alphanumeric'
    assert '1920x1080-Artbeats-3-v2.mp4' == directory.get_items()[0]

def test_directory_sort_date_modified(directory):
    directory.sort = 'Date Modified'
    assert 'short_fast_start_5Mbps' == directory.get_items()[0]

if __name__ == '__main__':
    pytest.main(["--log-level=INFO", "--log-file=directory_pytest.log", "--log-format='%(asctime)s - %(levelname)s - %(message)s"])