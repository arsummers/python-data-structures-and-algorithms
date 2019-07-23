import pytest
from queue_with_stacks import Stack, PseudoQueue
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
    
    assert s.pop() == 'c'

@pytest.mark.skip('fill')
def test_enqueue_empty_stack():
    q1 = PseudoQueue()

    q1.enqueue('a')    

    assert q1.peek() == 'a'

@pytest.mark.skip('fill')
def test_enqueue_stack_multiple():
    q1 = PseudoQueue()
    

    q1.enqueue('a')    
    q1.enqueue('b')    
    q1.enqueue('c')    

    assert q1.peek() == 'a'

@pytest.mark.skip('fill')
def test__dequeue_stack_of_one():
    q1 = PseudoQueue()

    q1.enqueue('a')    
    q1.enqueue('b')    
    q1.enqueue('c') 

    assert q1.dequeue() == 'a'

@pytest.mark.skip('fill')
def test_dequeue_empty_stack():
    q1 = PseudoQueue()

    assert q1.dequeue() == 'empty queue'