import pytest
from tree import BinarySearchTree

def test_exists():
    assert BinarySearchTree

def test_add_to_empty():
    tree = BinarySearchTree()
    tree.add(50)
    assert tree.root.value == 50


def test_add_smaller():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)

    assert tree.root.value == 50
    assert tree.root.left.value == 25

def test_add_larger():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(75)

    assert tree.root.value == 50
    assert tree.root.right.value == 75

def test_bigger_tree():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(25)
    tree.add(30)
    tree.add(60)
    tree.add(55)

    assert tree.root.value == 50
    assert tree.root.left.value == 25
    assert tree.root.right.value == 60
    assert tree.root.right.left.value == 55
    assert tree.root.left.right.value == 30

# def test_contains():
#     tree = BinarySearchTree()
#     tree.add(50)
#     assert tree.contains(50)

# def test_not_contains():
#     tree = BinarySearchTree()
#     tree.add(50)
#     assert not tree.contains(75)

