from stack_and_queue import __version__
from stack_and_queue.stack import Stack
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_stack(stack):
    assert stack.is_empty()

def test_push_to_stack(stack):
    expected = 7
    actual = stack.top.value
    assert expected == actual

def test_pop_from_stack(stack):
    expected = 7
    actual = stack.pop()
    assert expected == actual

@pytest.fixture
def stack():
    stack=Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)

    return stack

