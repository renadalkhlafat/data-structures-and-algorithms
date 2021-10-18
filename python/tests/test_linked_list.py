from linked_list.linked_list import Node,LinkedList

import pytest

def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
  with pytest.raises(TypeError):
    node = Node()

def test_new_linked_list_is_empty():
    #Arrange
  expected = None
    #Act
  ll = LinkedList()
  actual = ll.head
    #Assert
  assert actual == expected

# @pytest.mark.skip('todo')
def test_linked_list_insert_one_node():
    # Arrange
  expected = 1
    # Act
  ll = LinkedList()
    # Assert
  actual = ll.insert(2)

def test_linked_list_insert_multie_nodes():
    # Arrange
  expected = 3
    # Act
  ll = LinkedList()
    # Assert
  node1=ll.insert(1)
  node2 = ll.insert(2)

def test_linked_contain():
     # Arrange
    expected = True
    ll = LinkedList()
    x= ll.insert(2)
    # Act
    actual = ll.__contains__(2)
    #Assert
    assert expected == actual

def test_linked_not_contain():
     # Arrange
    expected = False
    ll = LinkedList()
    node1= ll.insert(2)
    node2= ll.insert(0)
    node3= ll.insert(6)
    # Act
    actual = ll.__contains__(1)
    #Assert
    assert expected == actual

def test__str__():
    # Arrange
    expected = "{ a } -> { b } -> { c } -> NULL"
    ll = LinkedList()
    # Act
    node1= ll.insert("c")
    node2= ll.insert("b")
    node3= ll.insert("a")

    actual= str(ll)
    #Assert
    assert actual == expected

def test_append_one():
    # Arrange
    expected ="{ 2 } -> { 5 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    node1 = ll.insert(2)
    node2 = ll.append(5)

    actual= str(ll)
    #Assert
    assert actual == expected


def test_append_multie_nodes():
    # Arrange
  expected ="{ 1 } -> { 5 } -> { 6 } -> NULL"
    # Act
  ll = LinkedList()
    # Assert
  node1=ll.insert(1)
  node2 = ll.append(5)
  node3 = ll.append(6)
  actual= str(ll)
    #Assert
  assert actual == expected

def test_insert_before_first_node():
    # Arrange
  expected ="{ 3 } -> { 5 } -> { 1 } -> NULL"
    # Act
  ll = LinkedList()
    # Assert
  node1=ll.insert(1)
  node1=ll.insert(3)
  node2 = ll.insert_before(5,1)
  actual= str(ll)
    #Assert
  assert actual == expected

def test_insert_before_middle_node():
    # Arrange
  expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    # Act
  ll = LinkedList()
    # Assert
  node1=ll.insert(1)
  node1=ll.insert(3)
  node2 = ll.insert_before(5,3)
  actual= str(ll)
    #Assert
  assert actual == expected

def test_insert_before_empty_list():
    # Arrange
  expected ="Empty linked list"
    # Act
  ll = LinkedList()
    # Assert

  node2 = ll.insert_before(5,1)
  actual= str(ll)
    #Assert
  assert actual == expected

def test_insert_after_list_tile():
    # Arrange
  expected ="This the linked list tile"
    # Act
  ll = LinkedList()
    # Assert
  node1= ll.insert(5)
  node2 = ll.insert(4)
  actual= ll.insert_after(5,4)
    #Assert
  assert actual == expected

def test_insert_after_middle_node():
    # Arrange
  expected ="{ 5 } -> { 3 } -> { 1 } -> NULL"
    # Act
  ll = LinkedList()
    # Assert
  node1=ll.insert(1)
  node1=ll.insert(3)
  node2 = ll.insert_after(5,3)
  actual= str(ll)
    #Assert
  assert actual == expected

def test_insert_after():
    # Arrange
  expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    # Act
  ll = LinkedList()
    # Assert
  node1= ll.insert(5)
  node2 = ll.insert(1)
  actual= ll.insert_after(3,1)
    #Assert
  assert actual == expected
