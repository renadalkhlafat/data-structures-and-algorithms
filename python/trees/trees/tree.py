"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Node_:
  def __init__ (self,data):
    self.data = data
    self.child = []
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

  def breadth_first(self):
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

def fizz_buzz(node):

    if not node.data % 5 and not node.data % 3 :
        return "FizzBuzz"
    elif not node.data % 3 :
        return "Fizz"
    elif not node.data % 5 :
        return "Buzz"
    else :
        return str(node.data)

def tree_fizz_buzz(k_tree):
    """
    Determine whether or not the value
    of each node is divisible by 3, 5 or both
    - If the value is divisible by 3, replace the value with “Fizz”
    - If the value is divisible by 5, replace the value with “Buzz”
    - If the value is divisible by 3 and 5,replace the value with “FizzBuzz”
    - If the value is not divisible by 3 or 5,simply turn the number into a String

    Input : K-ary tree
    output : new k-ary tree
    """
    queue = Queue()
    queue.enqueue(k_tree.root)

    while queue.peek():
      front = queue.dequeue()
      front.data = fizz_buzz(front)

      for child in front.child:
        queue.enqueue(child)

    return k_tree


def find_odd_sum(bTree):
  """
    find the sum of the odd numbers

    input : binary tree
    return : number
  """
  sum = 0

  def walk(node):
    nonlocal sum
    if node.data.isdigit() and node.data % 2 :
        sum += node.data
    if node.left :
      walk(node.left)
    if node.right:
        walk(node.right)
  walk (bTree.root)
  return sum

def k_ary_bfs(tree):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        """
        breadth = Queue()
        breadth.enqueue(tree.root)

        list_of_items = []
        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]
            if front.child:
                for item in front.child:
                    breadth.enqueue(item)
        return list_of_items


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(3)
    tree.add(15)
    tree.add(7)
    tree.add(10)

# print(find_odd_sum(tree))
