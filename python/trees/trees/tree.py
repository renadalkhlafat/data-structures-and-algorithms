"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

  def __init__(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    breadth = Queue()
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains in pre_order

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to trivarsal tree in in_order

    input : None

    output : tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
    return list_of_items

  def get_max(self):
    """
    Find the maximum value stored in the tree.

    Arguments: none

    Returns: number
    """
    if not self.root:
        raise Exception("Empty Tree !!!")

    # if not self.root.right and not self.root.left :
    #     return self.root.data
    self.max_num=self.root.data
    def max_item(node):
        if node.data>self.max_num:
            self.max_num= node.data
        if node.left:
            max_item(node.left)
        if node.right:
            max_item(node.right)
        return self.max_num

    return max_item(self.root)

class BinarySearchTree(BinaryTree):
    """
    class to hold adding and searching staff

    methods :
        - add()
        - contains()
    """
    def __init__(self):
        super().__init__()

    def add(self,value):
        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right

    def __contains__(self,value):
        """
        search for a value in the tree

        input : value

        output : True/False
        """
        if not self.root:
            raise Exception("Empty Tree !!!")

        else:
            temp = self.root
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right
