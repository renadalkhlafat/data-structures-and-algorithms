from stack_and_queue import __version__
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def stack():
    stack=Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)

    return stack

