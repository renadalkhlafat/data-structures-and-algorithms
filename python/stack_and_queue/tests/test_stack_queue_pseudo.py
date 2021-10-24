from stack_and_queue.stack_queue_pseudo import PseudoQueue
import pytest


def test_enqueue():
    expected = "[ 5 ] ->  Null"
    pesudo_queue = PseudoQueue()
    pesudo_queue.enqueue(5)
    actual = str(pesudo_queue)
    assert expected == actual


# @pytest.mark.skip('todo')
def test_multiple_enqueues(pesudo_queue):
    expected = "[ 2 ] -> [ 3 ] -> [ 5 ] ->  Null"
    actual = str(pesudo_queue)
    assert expected == actual


def test_dequeue(pesudo_queue):
    expected ="[ 2 ] -> [ 3 ] ->  Null"
    pesudo_queue.dequeue()
    actual = str(pesudo_queue)
    assert expected == actual


def test_multiple_dequeues(pesudo_queue):
    expected ="[ 2 ] ->  Null"
    pesudo_queue.dequeue()
    pesudo_queue.dequeue()
    actual = str(pesudo_queue)
    assert expected == actual


@pytest.fixture
def pesudo_queue():
    pesudo_queue = PseudoQueue()
    pesudo_queue.enqueue(5)
    pesudo_queue.enqueue(3)
    pesudo_queue.enqueue(2)

    return pesudo_queue
