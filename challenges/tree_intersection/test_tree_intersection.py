import pytest
from tree import BinaryTree, Node
from tree_intersection import tree_intersection

def test_exists():
    assert BinaryTree
    assert Node
    assert tree_intersection

@pytest.fixture()
def tree_1():
    two = Node(2)
    three = Node(3)
    five = Node(5)
    six = Node(6)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
  
    ten.left = eleven
    ten.right = five
    eleven.left = three
    eleven.right = two
    five.left = six
    five.right = nine
    

    arbor = BinaryTree()
    arbor.root = ten

    return arbor

@pytest.fixture()
def tree_2():
    one =  Node(1)
    two = Node(2)
    six = Node(6)
    ten = Node(10)
    eleven = Node(11)
    twenty = Node(20)
    twentyfive = Node(25)
  
    two.left = one
    two.right = twentyfive
    one.left = six
    one.right = ten
    twentyfive.left = eleven
    twentyfive.right = twenty

    arbor = BinaryTree()
    arbor.root = two

    return arbor

@pytest.fixture()
def empty_tree():
    empty_node = None
    arbor = BinaryTree()
    arbor.root = empty_node
    return arbor

@pytest.fixture()
def empty_tree2():
    empty_node = None
    arbor = BinaryTree()
    arbor.root = empty_node
    return arbor

def test_fixture_tree_1(tree_1):
    assert tree_1

def test_fixture_tree_2(tree_2):
    assert tree_2

def test_tree(tree_1, tree_2):
    
    assert tree_intersection(tree_1, tree_2) == [11, 2, 10, 6]

def test_none_tree(empty_tree, empty_tree2):
    assert tree_intersection(empty_tree, empty_tree2) == []