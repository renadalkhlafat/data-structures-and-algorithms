from hash_table import HashTable
from tree import BinaryTree

def tree_intersection(first_tree , second_tree):
    tree1 = first_tree.pre_order()
    tree2 = second_tree.pre_order()

    if not tree1 and not tree2:
        raise Exception("Empty trees !!!")
    if not tree1 or not tree2:
        raise Exception("There is no another tree to find the intersection")
    values_founded =[]
    hash_table = HashTable()
    for node in tree1:
        hash_table.add(str(node),node)
    for node in tree2:
        if hash_table.contains(str(node)):
            values_founded.append(node)
        else :
            hash_table.add(str(node),node)

    if not values_founded:
        return "there is no intersection between these trees"
    return values_founded

tree1=BinaryTree()
tree1.add(150)
tree1.add(100)
tree1.add(250)
tree1.add(75)
tree1.add(160)
tree1.add(200)
tree1.add(350)
tree1.add(125)
tree1.add(175)
tree1.add(300)
tree1.add(500)

tree2=BinaryTree()

tree2.add(42)
tree2.add(100)
tree2.add(600)
tree2.add(15)
tree2.add(160)
tree2.add(200)
tree2.add(350)
tree2.add(125)
tree2.add(175)
tree2.add(4)
tree2.add(500)


print(tree_intersection(tree1,tree2))
