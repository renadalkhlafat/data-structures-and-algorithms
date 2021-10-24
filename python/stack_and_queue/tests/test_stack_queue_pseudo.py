from stack_and_queue.stack_queue_pseudo import PseudoQueue

def test_enqueue():
    expected = 5
    queue = PseudoQueue()
    queue.enqueue(5)
    actual = queue.rear.data
    assert expected == actual
