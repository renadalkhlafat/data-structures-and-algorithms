def insertionSort(my_list):
    n = len(my_list)
    for item in range(1, n):
        j = item - 1
        temp = my_list[item]
        while j >= 0 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            j = j-1

        my_list[j+1] = temp
    return my_list

print(insertionSort([5, 4, 1, 9]))
