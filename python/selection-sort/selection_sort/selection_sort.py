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
