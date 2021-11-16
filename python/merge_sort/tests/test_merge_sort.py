from merge_sort import __version__
from merge_sort.merge_sort import mergeSort


def test_version():
    assert __version__ == '0.1.0'


def test_merge_sort():
    expected = [4, 8, 15, 16, 23, 42]
    list = [8, 4, 23, 42, 16, 15]
    actual = mergeSort(list)
    assert actual == expected


def test_merge_sort_case2():
    expected = [5, 5, 5, 7, 7, 7]
    list = [5, 12, 7, 5, 5, 7]
    actual = mergeSort(list)
    assert actual == expected
