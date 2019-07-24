import pytest
from fifo_animal_shelter import Queue, FifoAnimalShelter

def test_enqueue_pets():
    dogs = ['pug', 'lab', 'beagle']
    cats = ['tabby', 'calico', 'bengal']

    dog_queue = Queue()
    cat_queue = Queue()

    for dog in dogs:
        dog_queue.enqueue(dog)
    
    for cat in cats:
        cat_queue.enqueue(cat)

    assert dog_queue.peek() == 'pug'
    assert cat_queue.peek() == 'tabby'
    