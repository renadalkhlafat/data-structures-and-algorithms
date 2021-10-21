from stack_and_queue.queue import Queue
import pytest

def test_enqueues_into_queue():
    expected = 5
    queue = Queue()
    queue.enqueue(5)
    actual = queue.rear.data
    assert expected == actual

def test_multiple_enqueues_into_queue(queue):
    expected = 8
    actual = queue.rear.data
    assert expected == actual

def test_dequeue_from_queue(queue):
    expected = 2
    actual = queue.dequeue()
    assert expected == actual

def test_peek_from_queue(queue):
    expected = 2
    actual = queue.peek()
    assert expected == actual

def test_peek_from_queue_after_multiple_dequeues(queue):
    node1= queue.dequeue()
    node2= queue.dequeue()
    node3= queue.dequeue()
    node4= queue.dequeue()
    assert queue.is_empty() == True

def test_instantiate_an_empty_queue():
    queue = Queue()
    assert queue.front and queue.rear == None

def test_peek_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.peek()

def test_peek_from_empty_queue():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.dequeue()




@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)

    return queue

