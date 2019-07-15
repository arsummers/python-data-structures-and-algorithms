from linked_list import LinkedList, Node

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
    ll.insert('sealion')
    ll.insert('black bear')
    ll.insert('fox')
    assert ll.includes_val('fox') == True

def test_includes_val_false():
    ll = LinkedList()
    ll.insert('sealion')
    ll.insert('black bear')
    ll.insert('harp seal')

    assert ll.includes_val('rhino') == False

def test_str():
    ll = LinkedList()
    ll.insert('leopard')
    ll.insert('wolf ')
    ll.insert('bear ')
    assert ll.__str__() == 'bear wolf leopard'

# TESTS FOR LL_INSERTIONS

def test_add_single_node_to_end_of_list():
    ll = LinkedList()
    ll.insert('pig')
    ll.append_val('sheep')
    assert ll.head.animal_value == 'pig'
    assert ll.head.next.animal_value == 'sheep'

def test_add_multiple_nodes_to_end_of_list():
    ll = LinkedList()
    ll.insert('sheep')
    ll.insert('pig')
    ll.append_val('cow')
    assert ll.head.animal_value == 'pig'
    assert ll.head.next.animal_value == 'sheep'
    assert ll.head.next.next.animal_value == 'cow'


def test_insert_before_middle():
    ll = LinkedList()
    ll.insert('sheep')
    ll.insert('pig')
    ll.insert_before('sheep', 'cow')
    assert ll.head.animal_value == 'pig'
    assert ll.head.next.animal_value == 'cow'
    assert ll.head.next.next.animal_value == 'sheep'
    
def test_insert_before_first_node():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')
    ll.insert_before('sheep', 'cow')
    assert ll.head.animal_value == 'cow'
    assert ll.head.next.animal_value == 'sheep'
    assert ll.head.next.next.animal_value == 'pig'

# Can successfully insert after a node in the middle of the linked list
def test_insert_after_middle():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')
    ll.insert_after('sheep', 'cow')
    assert ll.head.animal_value == 'sheep'
    assert ll.head.next.animal_value == 'cow'
    assert ll.head.next.next.animal_value == 'pig'

# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')
    ll.insert_after('pig', 'cow')
    assert ll.head.animal_value == 'sheep'
    assert ll.head.next.animal_value == 'pig'
    assert ll.head.next.next.animal_value == 'cow'