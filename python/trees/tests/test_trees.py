"""
Test binary tree class
"""
from python.trees.trees import tree
from trees import __version__
from trees.tree import BinaryTree, Node , BinarySearchTree
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_bfs():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for A,B,C,D
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs passed")

def test_bfs_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for A,B,C,D
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs_2 passed")

def test_pre_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["1", "2", "4", "3"]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_pre_order_ passed")

def test_post_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["4", "2", "3", "1"]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_post_order_ passed")

def test_in_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()
    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root = a_node
    # set expected list
    expected = ["4", "2", "1", "3"]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_in_order_ passed")

def test_empty_tree():
    expected = None
    tree = BinaryTree()
    actual = tree.root

    assert expected == actual

def test_tree_with_single_node():
    expected = "A"
    tree = BinaryTree()
    a_node = Node('A')
    tree.root = a_node
    actual = tree.root.data

    assert actual == expected

# ******************** binary search tree tests **********************
def test_add_once():
     # Arrange
    # Create tree instance
    tree = BinarySearchTree()
    # add "A" to the tree
    tree.add('A')
    # set expected list
    expected = "A"
    # set actual to the tree root value
    actual = tree.root.data
    # assert actual is same as expected
    assert actual == expected

def test_add_twice():
    # Arrange
    # Create tree instance
    tree = BinarySearchTree()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    # set expected list
    expected = ["A","B"]
    # set actual to the tree root value
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected

def test_contains_value():
    # Arrange
    # Create tree instance
    tree = BinarySearchTree()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = True
    # set actual to the tree root value
    actual = tree.__contains__("B")
    # assert actual is same as expected
    assert actual == expected

def test_not_contains_value():
   # Arrange
    # Create tree instance
    tree = BinarySearchTree()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = False
    # set actual to the tree root value
    actual = tree.__contains__("E")
    # assert actual is same as expected
    assert actual == expected

def test_search_in_empty_tree():
   with pytest.raises(Exception):
       tree = BinarySearchTree()
       actual = tree.__contains__("O")

def test_add_left_and_right_nodes():
    # Arrange
    # Create tree instance
    tree = BinarySearchTree()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = ["A","B","C"]
    # set actual to the tree root value
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected

#************************** Test get-max method ***********************
def get_max_happy_path():
    #Arrange
    expected = 5
    #Act
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(1)
    tree.add(5)
    tree.add(2)

    actual = tree.get_max()

    assert actual == expected

def get_max_from_empty_tree():
    with pytest.raises(Exception):
        tree = BinaryTree()
        actual = tree.get_max()
