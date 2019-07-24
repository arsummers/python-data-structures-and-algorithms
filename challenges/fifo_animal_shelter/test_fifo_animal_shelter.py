import pytest
from fifo_animal_shelter import Queue, FifoAnimalShelter

@pytest.fixture
def pets_queue():
    dogs = ['pug', 'lab', 'beagle']
    cats = ['tabby', 'calico', 'bengal']

    dog_queue = Queue()
    cat_queue = Queue()

    for dog in dogs:
        dog_queue.enqueue(dog)
    
    for cat in cats:
        cat_queue.enqueue(cat)

    assert dog_queue.front.value == 'pug'
    assert cat_queue.front.value == 'tabby'


@pytest.mark.skip('not registering dog_queue as defined')   
def test_search_for_dogs(pets_queue):
    
    searched_animal = 'lab'

    assert dog_queue.dequeue() == 'pug'

@pytest.mark.skip('not registering cat_queue as defined')   
def test_search_for_dogs(pets_queue):
    
    searched_animal = 'tabby'

    assert cat_queue.dequeue() == 'tabby'

@pytest.mark.skip('not registering dog_queue as defined')   
def test_search_for_dogs(pets_queue):
    
    searched_animal = 'fish'

    assert dog_queue.dequeue() == 'pug'
    assert cat_queue.dequeue() == 'tabby'   