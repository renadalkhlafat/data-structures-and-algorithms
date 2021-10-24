from stack_and_queue.stack_queue_pseudo import PseudoQueue
import pytest


def test_enqueue():
    expected = 5
    pesudo_queue = PseudoQueue()
    pesudo_queue.enqueue(5)
    actual = pesudo_queue.rear.data
    assert expected == actual

def test_multiple_enqueues(pesudo_queue):
    expected = 3
    actual = pesudo_queue.rear.data
    assert expected == actual


@pytest.fixture
def queue():
    pesudo_queue =PseudoQueue()
    pesudo_queue.enqueue(3)
    pesudo_queue.enqueue(6)
    pesudo_queue.enqueue(8)

    return pesudo_queue
