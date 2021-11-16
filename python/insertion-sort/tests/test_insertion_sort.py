from insertion_sort import __version__
from insertion_sort.insertion_sort import insertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_selection_sort_first_case():
    expected =[-2,5,8,12,18,20]
    arr = [20,18,12,8,5,-2]
    actual = insertionSort(arr)
    assert actual == expected

def test_selection_sort_second_case():
    expected =[5,5,5,7,7,12]
    arr = [5,12,7,5,5,7]
    actual = insertionSort(arr)
    assert actual == expected

def test_selection_sort_third_case():
    expected =[2,3,5,7,11,13]
    arr = [2,3,5,7,13,11]
    actual = insertionSort(arr)
    assert actual == expected
