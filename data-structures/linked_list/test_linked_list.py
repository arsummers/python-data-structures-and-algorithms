from linked_list import LinkedList, Node
import pytest

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
    assert ll.head.node_value == 'dog'

# checks that the head of the list can be replaced
def test_insert_into_empty_list_again():
    ll = LinkedList()
    ll.insert('cat')
    assert ll.head.node_value == 'cat'

def test_insert_fox_into_seal():
    ll = LinkedList()
    ll.insert('seal')
    ll.insert('fox')
    assert ll.head.node_value == 'fox'
    assert ll.head.next.node_value == 'seal'

def test_insert_three_nodes():
    ll = LinkedList()
    ll.insert('sealion')
    ll.insert('black bear')
    ll.insert('harp seal')
    assert ll.head.node_value == 'harp seal'
    assert ll.head.next.node_value == 'black bear'
    assert ll.head.next.next.node_value == 'sealion'


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
    ll.insert('goat')
    ll.append_val('sheep')
    assert ll.head.node_value == 'goat'
    assert ll.head.next.node_value == 'pig'
    assert ll.head.next.next.node_value == 'sheep'

def test_add_multiple_nodes_to_end_of_list():
    ll = LinkedList()
    ll.insert('sheep')
    ll.insert('pig')
    ll.append_val('cow')
    ll.append_val('goat')
    assert ll.head.node_value == 'pig'
    assert ll.head.next.node_value == 'sheep'
    assert ll.head.next.next.node_value == 'cow'
    assert ll.head.next.next.next.node_value == 'goat'

@pytest.mark.skip('NEED HELP - while loop issues')
def test_insert_before_middle():
    ll = LinkedList()
    ll.insert('sheep')
    ll.insert('pig')

    ll.insert_before('sheep', 'cow')
    assert ll.head.node_value == 'pig'
    assert ll.head.next.node_value == 'cow'
    assert ll.head.next.next.node_value == 'sheep'

@pytest.mark.skip('NEED HELP - while loop issues')    
def test_insert_before_first_node():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')

    ll.insert_before('sheep', 'cow')
    assert ll.head.node_value == 'cow'
    assert ll.head.next.node_value == 'sheep'
    assert ll.head.next.next.node_value == 'pig'

@pytest.mark.skip('NEED HELP - while loop issues')
def test_insert_after_middle():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')
    ll.insert_after('sheep', 'cow')

    assert ll.head.node_value == 'sheep'
    assert ll.head.next.node_value == 'cow'
    assert ll.head.next.next.node_value == 'pig'

@pytest.mark.skip('NEED HELP - while loop issues')
def test_insert_after_last_node():
    ll = LinkedList()
    ll.insert('pig')
    ll.insert('sheep')

    targeted_node = ll.head.next
    ll.insert_after(targeted_node, 'cow')
    assert ll.head.node_value == 'sheep'
    assert ll.head.next.node_value == 'pig'
    assert ll.head.next.next.node_value == 'cow'

# TESTS FOR Kth FROM END

# Where k is greater than the length of the linked list
@pytest.mark.skip('NEED HELP - while loop issues')
def test_k_greater_than_list_length():
    ll = LinkedList()
    ll.insert('d')
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    # k = 5
    assert ll.head.node_value == 'a'
    assert ll.head.next.next.next.node_value == 'd'
    assert ll.kth_from_end(6) == ValueError


# Where k and the length of the list are the same
@pytest.mark.skip('NEED HELP - while loop issues')
def test_k_same_as_length():
    ll = LinkedList()
    ll.insert('d')
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    assert ll.head.node_value == 'a'
    assert ll.head.next.next.next.node_value == 'd'
    assert ll.kth_from_end(3) == 'a'

# Where k is not a positive integer
@pytest.mark.skip('NEED HELP - while loop issues')
def test_k_not_positive():
    ll = LinkedList()
    ll.insert('d')
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    assert ll.head.node_value == 'a'
    assert ll.head.next.next.next.node_value == 'd'
    assert ll.kth_from_end(0) == 'd'

# Where the linked list is of a size 1
@pytest.mark.skip('NEED HELP - while loop issues')
def test_length_size_one():
    ll = LinkedList()
    ll.insert('a')

    assert ll.head.node_value == 'a'
    assert ll.kth_from_end(0) == 'a'

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_k_in_middle():
    ll = LinkedList()
    ll.insert('d')
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    assert ll.head.node_value == 'a'
    assert ll.head.next.next.next.node_value == 'd'
    assert ll.kth_from_end(1) == 'c'