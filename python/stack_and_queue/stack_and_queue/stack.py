from _pytest.recwarn import T
from stack_and_queue.node import Node
class Stack:
    """
    class will implement the Stack data structure

    Attribute:
    top ->  the top of the stack.

    Methods:
    push() -> add node to stack
        arguments -> value
        return -> none

    pop() -> remove node from stack
        arguments -> none
        return -> the poped node value

    peek() -> view the top value
        arguments ->none
        return -> top node value

    is_empty() ->
        arguments -> none
        return -> True if the stack empty , False if not

    """
    def __init__(self) :
       self.top = None

    def push(self ,value):
        node=Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top :
            raise Exception("You can't pop from Empty Stack !!!")
        else :
           temp = self.top
           self.top = self.top.next
           temp.next = None
        return temp.data

    def peek(self):
        if not self.top :
            raise Exception("Empty Stack !!!")
        else :
            return self.top.data

    def is_empty(self):
        if not self.top:
            return True
        return False
