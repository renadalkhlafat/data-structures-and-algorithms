from hash_table.hash_table import HashTable


def left_join(first_hashmap:HashTable, second_hashmap:HashTable):
    final_hashmap = []
    for item in first_hashmap._HashTable__buckets:
        if item :
            current = item.head
            left_join = []
            while current:
                left_join.append(current.value[0])
                left_join.append(current.value[1])
                if second_hashmap.contains(current.value[0]):
                    left_join.append(second_hashmap.get(current.value[0]))
                else:
                    left_join.append(None)

                current = current.next

            final_hashmap.append(left_join)
    return final_hashmap

first_hash_table = HashTable()
# # first_hash_table.add("person", "23")
# # first_hash_table.add("person1", "30")
# # first_hash_table.add("person2", "27")
# # first_hash_table.add("person3", "18")
# # first_hash_table.add("person4", "19")
second_hash_table = HashTable()
# second_hash_table.add("person", "45")
# second_hash_table.add("person1", "25")
# second_hash_table.add("person2", "19")
# second_hash_table.add("person4", "9")

print(left_join(first_hash_table, second_hash_table))
