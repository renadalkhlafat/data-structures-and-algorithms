from stack_and_queue.node import Node
class Queue:
    """
    class will implement the Queue data structure

    Attribute:
    front -> the first Node of the queue.
    rear ->  the last Node of the queue.

    Methods:
    enqueue() -> add node to the queue
        arguments -> value
        return -> none

    dequeue () -> remove node from the queue
        arguments -> none
        return -> the poped node value

    peek() -> view the value of the front Node in the queue
        arguments ->none
        return -> top node value

    is_empty() ->
        arguments -> none
        return -> True if the queue empty , False if not

    """
    def __init__(self) :
       self.front = None
       self.rear = None

    def enqueue(self ,value):
        node = Node(value)
        if not self.rear:
           self.front = node
           self.rear= node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front :
            raise Exception("You can't dequeue from empty Queue !!!")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None

        return temp.data

    def peek(self):
        if not self.front :
            raise Exception("Empty Queue !!!")
        else :
            return self.front.data

    def is_empty(self):
        if not self.front:
            return True
        return False
