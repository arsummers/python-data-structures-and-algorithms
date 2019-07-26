import pytest
from tree import BinaryTree, Node

def test_exists():
    assert BinaryTree
    assert Node

@pytest.fixture
def tree():
    one =  Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
  
    one.left = two
    one.right = three
    three.left = four
    three.right = five
    two.left = six
    six.right = seven
    seven.left = eight
    seven.right = nine

    arbor = BinaryTree
    arbor.root = one

    return arbor