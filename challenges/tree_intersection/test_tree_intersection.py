import pytest
from tree import BinaryTree, Node

def test_exists():
    assert BinaryTree
    assert Node

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
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
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

def test_fixture_tree_1(tree_1):
    assert tree_1

def test_fixture_tree_2(tree_2):
    assert tree_2

