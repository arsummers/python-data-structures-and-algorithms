import pytest
from stacks_and_queues import Stack, Queue

@pytest.fixture
def Node():
    pass

@pytest.fixture
def even_lst():
    pass

@pytest.fixture
def odd_lst():
    pass


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

    s.pop('a')
    
    assert s.peek() == 'b'

# Can successfully empty a stack after multiple pops
def test_pop_stack_to_empty():
    s = Stack()

    pass

# Can successfully peek the next item on the stack
def test_peek_nth_item():
    s = Stack()

    pass

# Can successfully instantiate an empty stack
def test_instantiate_empty_stack():
    s = Stack()

    assert s.peek() is None

# Can successfully enqueue into a queue
def test_enqueue_single_value():
    q = Queue()

    q.enqueue('a')    
    
    assert q.peek() == 'a'

# Can successfully enqueue multiple values into a queue
def test_enqueue_multiple_values():
    q = Queue()

    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    assert q.peek() == 'c'
  
# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    q = Queue()

    pass

# Can successfully peek into a queue, seeing the expected value
def test_peek_into_queue():
    q = Queue()

    q.enqueue('a')

    assert q.peek == 'a'

# Can successfully empty a queue after multiple dequeues
def test_dequeue_queue_to_empty():
    q = Queue()

    pass

# Can successfully instantiate an empty queue
def test_instantiate_empty_queue():
    q = Queue()

    assert q.peek() is None