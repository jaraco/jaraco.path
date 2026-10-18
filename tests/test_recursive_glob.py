from jaraco.path import recursive_glob


def test_recursive_glob_includes_root_and_descendants(tmp_path):
    root_file = tmp_path / 'root.txt'
    root_file.write_text('root', encoding='utf-8')
    nested = tmp_path / 'subdir' / 'nested'
    nested.mkdir(parents=True)
    nested_file = nested / 'child.txt'
    nested_file.write_text('child', encoding='utf-8')
    (nested / 'ignore.py').touch()

    assert set(recursive_glob(str(tmp_path), '*.txt')) == {
        str(root_file),
        str(nested_file),
    }


def test_recursive_glob_without_subdirectories(tmp_path):
    target = tmp_path / 'only.txt'
    target.touch()
    assert list(recursive_glob(str(tmp_path), '*.txt')) == [str(target)]
