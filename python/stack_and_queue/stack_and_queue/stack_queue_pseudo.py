from stack_and_queue.stack import Stack


class PseudoQueue:
    """
    class will implement standard queue using Stack class

    Methods :
    enqueue() ->  Inserts value into the PseudoQueue, using a first-in, first-out approach.
        Arguments -> value
        return -> None


    dequeue() ->Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        Arguments -> none
        return -> the poped node value

    str()-> print out the queue
        Arguments -> none
        return -> the queue

    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)
        self.rear= self.stack1.top.data

    def dequeue(self):
        if self.stack1.top:
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            value_poped =self.stack2.pop()
            self.front = self.stack2.top
            self.stack1 =Stack()
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
            return value_poped
        else:
            return "Empty queue !!!"



    def __str__(self):
        return "queue"

# q=PseudoQueue()
# q.enqueue(5)
# q.enqueue(3)
# q.enqueue(2)

# print(q.rear)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.front)
