from hash_table.hash_table import HashTable


def left_join(first_hashmap, second_hashmap):
    final_hashmap = []
    for item in first_hashmap.itervalues():
        if item :
            current = item.head
            list_join = []
            while current:
                list_join.append(current.value[0])
                list_join.append(current.value[1])
                if second_hashmap.contains(current.key.value[0]):
                    list_join.append(second_hashmap.get(current.value[0]))
                else:
                    list_join.append(None)

                current = current.next

            final_hashmap.append(list_join)
    return final_hashmap

