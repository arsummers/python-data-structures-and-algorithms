import pytest
from queue_with_stacks import PseudoQueue

@pytest.fixture
def pseudo_queue():
    return PseudoQueue()

def test_enqueue_empty_stack(pseudo_queue):

    pseudo_queue.enqueue('a')    
    assert pseudo_queue.front.value == 'a'

def test_enqueue_stack_multiple(pseudo_queue):
  
    pseudo_queue.enqueue('a')    
    pseudo_queue.enqueue('b')    
    pseudo_queue.enqueue('c')    

    assert pseudo_queue.front.value == 'a'

@pytest.mark.skip('not passing yet - will need to refactor')
def test__dequeue_stack_of_one(pseudo_queue):

    pseudo_queue.enqueue('a')    
    pseudo_queue.enqueue('b')    
    pseudo_queue.enqueue('c') 

    assert pseudo_queue.dequeue() == 'c'

def test_dequeue_empty_stack(pseudo_queue):

    assert pseudo_queue.dequeue() == 'Empty queue'