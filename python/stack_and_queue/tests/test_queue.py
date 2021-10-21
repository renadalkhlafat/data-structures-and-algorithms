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
    actual = queue.front.data
    assert expected == actual




@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)

    return queue

