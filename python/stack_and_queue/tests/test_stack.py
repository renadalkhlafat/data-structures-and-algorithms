from stack_and_queue import __version__
from stack_and_queue.stack import Stack
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

def test_instantiate_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True


def test_not_empty_stack(stack):
    assert stack.is_empty() == False


# @pytest.mark.skip('todo')
def test_push_to_stack(stack):
    expected = 7
    actual = stack.top.data
    assert expected == actual

def test_push_one_node_onto_stake():
    expected = 1
    stack = Stack()
    stack.push(1)
    actual = stack.top.data
    assert expected == actual

# @pytest.mark.skip('todo')
def test_pop_from_not_empty_stack(stack):
    expected = 7
    actual = stack.pop()
    assert expected == actual

def test_pop_all_nodes_from_not_empty_stack(stack):
    node1 = stack.pop()
    node2 = stack.pop()
    node3 = stack.pop()
    node4 = stack.pop()
    assert stack.is_empty() == True

# @pytest.mark.skip('todo')
def test_pop_from_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()


# @pytest.mark.skip('todo')
def test_peek_from_not_empty_stack(stack):
    expected = 7
    actual = stack.peek()
    assert expected == actual

def test_peek_net_value_from_not_empty_stack(stack):
    expected = 5
    node = stack.pop()
    actual = stack.peek()
    assert expected == actual


# @pytest.mark.skip('todo')
def test_peek_from_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)

    return stack
