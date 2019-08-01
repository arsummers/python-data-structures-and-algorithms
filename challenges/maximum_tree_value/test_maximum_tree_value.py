import pytest
from maximum_tree_value import BinaryTree, Node, find_maximum_value, find_maximum_value_other_way

def test_exists():
    assert BinaryTree
    assert Node

@pytest.fixture()
def tree():
    
    one =  Node(1)
    eleven = Node(11)
    thirtyfive = Node(35)
    fourtwenty = Node(420)
    fifteen = Node(15)
    six = Node(6)
    sixty = Node(60)
    seven = Node(7)
    eight = Node(8)
    ninetynine = Node(99)

    arbor = BinaryTree()
    arbor.root = one

    one.left = eleven
    eleven.left = fifteen
    fifteen.left = seven
    eleven.right = fourtwenty
    one.right = thirtyfive
    thirtyfive.right = six
    thirtyfive.left = sixty
    sixty.left = ninetynine
    sixty.right = eight

    return arbor

def test_fixture_tree(tree):
    assert tree

def test_single_max_value(tree):
     
    expected = 420
    actual = find_maximum_value(tree)
    assert expected == actual

    
def test_max_other_way(tree):
    expected = 420
    actual = find_maximum_value_other_way(tree)
    assert expected == actual


