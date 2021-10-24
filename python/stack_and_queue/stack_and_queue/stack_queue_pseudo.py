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
        pass

    def __str__(self):
        return "queue"

# q=PseudoQueue()
# q.enqueue(5)
# q.enqueue(3)
# q.enqueue(2)
# print(q.rear)
