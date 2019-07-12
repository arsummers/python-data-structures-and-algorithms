from linked_list import LinkedList, Node
# test animals to put into list from:https://en.wikipedia.org/wiki/List_of_carnivorans_by_population
# https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/

def does_exist():
    assert LinkedList()
    assert Node()
    assert __str__()

# Can successfully instantiate an empty linked list
def test_creation():
    ll = LinkedList()
    assert ll

def test_empy_list_creation():
    ll = LinkedList()
    assert ll.head is None

def test_insert_into_empty_list():
    ll = LinkedList()
    ll.insert('dog')
    assert ll.head.animal_value == 'dog'

# checks that the head of the list can be replaced
def test_insert_into_empty_list_again():
    ll = LinkedList()
    ll.insert('cat')
    assert ll.head.animal_value == 'cat'

def test_insert_fox_into_seal():
    ll = LinkedList()
    ll.insert('seal')
    ll.insert('fox')
    assert ll.head.animal_value == 'fox'
    assert ll.head.next.animal_value == 'seal'

def test_insert_three_animals():
    ll = LinkedList()
    ll.insert('sealion')
    ll.insert('black bear')
    ll.insert('harp seal')
    assert ll.head.animal_value == 'harp seal'
    assert ll.head.next.animal_value == 'black bear'
    assert ll.head.next.next.animal_value == 'sealion'


def test_includes_val_true():
    ll = LinkedList()
    if ll.includes_val('fox'):
        return True

def test_includes_val_false():
    ll = LinkedList()
    if ll.includes_val('rhino'):
        return False

def test_str():
    ll = LinkedList()
    ll.insert('leopard')
    ll.insert('wolf ')
    ll.insert('bear ')
    assert ll.__str__() == 'bear wolf leopard'
