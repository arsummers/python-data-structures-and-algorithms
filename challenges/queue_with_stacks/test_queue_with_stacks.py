import pytest
from queue_with_stacks import Stack
# Can successfully push onto a stack
def test_stack_push_one():
    s = Stack()
    s.push('a')
    assert s.peek() == 'a'

# Can successfully push multiple values onto a stack
def test_stack_push_multiple():
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')
    assert s.peek() == 'c'

# Can successfully pop off the stack
def test_stack_pop():
    s = Stack()

    s.push('a')
    s.push('b')
    s.push('c')

    s.pop()
    
    assert s.peek() == 'b'

@pytest.mark.skip('fill')
def test_enqueue_empty_stack():
    s1 = Stack()
    s2 = Stack()

    s1.enqueue('a')    

    assert s1.peek() == 'a'

@pytest.mark.skip('fill')
def test_enqueue_stack_multiple():
    s1 = Stack()
    s2 = Stack()

    s1.enqueue('a')    
    s1.enqueue('b')    
    s1.enqueue('c')    

    assert s1.peek() == 'a'

@pytest.mark.skip('fill')
def test__dequeue_stack_of_one():
    s1 = Stack()
    s2 = Stack()

    s1.enqueue('a')    
    s1.enqueue('b')    
    s1.enqueue('c') 

    assert dequeue() == 'a'

@pytest.mark.skip('fill')
def test_dequeue_empty_stack():
    s1 = Stack()
    s2 = Stack()

    assert dequeue() == 'empty stack'