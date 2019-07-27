import pytest
from tree import BinarySearchTree

def test_exists():
    assert BinarySearchTree

def test_add_to_empty():
    tree = BinarySearchTree()
    tree.add('orange')
    assert tree.root.value == 'orange'

@pytest.mark.skip()
def test_add_smaller():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)

    assert tree.root.value == 50
    assert tree.root.left.value == 25

@pytest.mark.skip()
def test_add_larger():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(75)

    assert tree.root.value == 50
    assert tree.root.right.value == 75

# def test_contains():
#     tree = BinarySearchTree()
#     tree.add(50)
#     assert tree.contains(50)

# def test_not_contains():
#     tree = BinarySearchTree()
#     tree.add(50)
#     assert not tree.contains(75)

