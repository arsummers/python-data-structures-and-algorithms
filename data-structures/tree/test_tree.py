import pytest
from tree import BinaryTree, Node

def test_exists():
    assert BinaryTree
    assert Node


@pytest.fixture()
def balanced_bst():
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)

    seven.left = five
    five.left = four
    five.right = six
    seven.right = nine
    nine.left = eight
    nine.right = ten

    full_tree = BinaryTree()
    full_tree.root = seven

    return full_tree


@pytest.fixture()
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

    arbor = BinaryTree()
    arbor.root = one

    return arbor

def test_fixture_tree(tree):
    assert tree

def test_pre_order(tree):
    expected = [1, 2, 6, 7, 8 , 9, 3, 4, 5]
    actual = tree.pre_order()

    assert expected == actual

def test_in_order(tree):
    expected = [6, 8, 7, 9, 2, 1, 4, 3, 5]
    actual = tree.in_order()

    assert expected == actual

def test_post_order(tree):
    expected = [8, 9 , 7, 6, 2, 4, 5, 3, 1]
    actual = tree.post_order()

    assert expected == actual



def test_bal_bst_pre_order(balanced_bst):
    expected = [7, 5, 4, 6, 9, 8, 10]
    actual = balanced_bst.pre_order()

    assert expected == actual

def test_bal_bst_in_order(balanced_bst):
    expected = [4, 5, 6, 7, 8, 9, 10]
    actual = balanced_bst.in_order()

    assert expected == actual


def test_bal_bst_post_order(balanced_bst):
    expected = [4, 6, 5, 8, 10, 9, 7]
    actual = balanced_bst.post_order()

    assert expected == actual