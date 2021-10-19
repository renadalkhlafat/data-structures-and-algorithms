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


    def kth_from_end(self, k):
        """
        Return the node’s value that is `k` places from the tail of the linked list.

        arguments:
        K : any

        returns: the value of the `k` places

        """
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
        value = length-k-1
        for i in range(length):
            if i == value:
                return current.data
            current = current.next


def zipLists(list1,list2):
    """
    Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

    arguments:
        K : any

    returns: the value of the `k` places

    """
    first_list = list1.head
    second_list = list2.head

    if not first_list and not second_list:
        return 'There is no lists to zip'
    elif  not first_list :
        return str(list2)
    elif not second_list:
        return str(list1)

    hold_node = ''
    while first_list and second_list:
        if second_list:
            hold_node = first_list.next
            first_list.next = second_list
            first_list = hold_node

        if first_list:
            hold_node = second_list.next
            second_list.next = first_list
            second_list = hold_node
    return str(list1)

if __name__ =="__main__":
    first_ll =LinkedList()
    first_ll.insert(1)
    first_ll.append(7)
    first_ll.append(4)
    first_ll.insert(0)
    first_ll.append(8)
    first_ll.append(9)

    second_ll =LinkedList()
    second_ll.insert(5)
    second_ll.append(3)
    second_ll.append(2)
    print(zipLists(first_ll,second_ll))

