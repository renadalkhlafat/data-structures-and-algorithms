from typing import Counter


class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

class LinkedList:
    """
    A class for creating instances of a Linked List.

    Data and other attributes defined here:

    head: Node | None

    Methods defined here

    insert(value: any)
    contains(value: any) -> bool
  """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """"
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        arguments:
        value : any

        returns: None
        """
        # create new node
        self.head = Node(value, self.head)

    def __contains__(self,value):
        """"
        contains search in the linked list for a given value , and return True if the value exist and return False not exist

        arguments:
        value : any

        returns: True if value int the list / False if the vlaue not exist
        """
        if self.head == None:
            return False
        else:
            p = self.head
            while p is not None:
                if p.data == value:
                    return True
                p = p.next
            return False

    def __str__(self):
        """
        to string method to print out the linked list in "{ a } -> { b } -> { c } -> NULL" format

        arguments:
        value : none

        returns: a string representing all the values in the Linked List
        """
        current =self.head
        result =''
        while current is not None:
            result += "{ " + str(current.data)+ " } -> "
            current = current.next
        result += 'NULL'
        return result

    def append (self,value):
        """
        to add a node to the end of the linked list

        arguments:
        value : any

        returns: none
        """
        node =Node(value)
        current = self.head
        if current :
            while current.next:
                current=current.next
            current.next=node
        else:
            self.head=node

    def insert_before(self ,newValue,valueToAddBefore):
        """
        adds a new node with the given new value immediately before the first node that has the value specified

        arguments:
        newValue : any
        valueToAddBefore : any

        returns: none

        """

        current =self.head
        if not current:
            return "NULL"
        while current.next:
            if current.next.data == valueToAddBefore:
                new_node =Node(newValue)
                new_node.next = current.next
                current.next=new_node
        current=current.next

    def insert_after(self ,newValue,valueToAddafter):
        """
        adds a new node with the given new value immediately after the first node that has the value specified

        arguments:
        newValue : any
        valueToAddBefore : any

        returns: if the linked list empty return 'Empty linked list' otherwise none

        """

        current =self.head
        if not current.next:
            return "This the linked list tile"
        while current.next:
            if current.data == valueToAddafter:
                new_node =Node(newValue)
                new_node.next = current.next
                current.next=new_node
        current=current.next


    def kthFromEnd(self, k):
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        current = self.head
        if k < 0:
            return "k must be non-negative number"
        elif k >= length:
            return 'Index out of range'
        count = length-k-1
        for i in range(length):
            if i == count:
                return current.data
            current = current.next
