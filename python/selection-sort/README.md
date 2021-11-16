# Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning

# Pseudocode
``` pseudo
SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
```
# Trace
**Example :** [20,18,12,8,5,-2]

# Code (python) :
```python
def selectionSort(my_list):
    n = len(my_list)
    for item in range(n):
        min = item
        for j in range(item + 1, n):
            if my_list[min] > my_list[j]:
                min = j
        my_list[item], my_list[min] = my_list[min], my_list[item]

    sorted_list = []
    for i in range(len(my_list)):
        sorted_list.append(my_list[i])
    return sorted_list

```

# Test :
```python
def test_selection_sort_first_case():
    expected =[-2,5,8,12,18,20]
    arr = [20,18,12,8,5,-2]
    actual = selectionSort(arr)
    assert actual == expected

def test_selection_sort_second_case():
    expected =[5,5,5,7,7,12]
    arr = [5,12,7,5,5,7]
    actual = selectionSort(arr)
    assert actual == expected

def test_selection_sort_third_case():
    expected =[2,3,5,7,11,13]
    arr = [2,3,5,7,13,11]
    actual = selectionSort(arr)
    assert actual == expected
```
