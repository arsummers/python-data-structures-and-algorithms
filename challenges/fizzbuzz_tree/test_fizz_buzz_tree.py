import pytest
from fizz_buzz_tree import BinaryTree, Node, fizz_buzz_tree

def test_exists():
    assert BinaryTree
    assert Node
    assert fizz_buzz_tree

@pytest.fixture()
def tree():
    fifteen =  Node(15)
    two = Node(2)
    twenty = Node(20)
    seven = Node(7)
    thirty_one = Node(31)
    nine = Node(9)
    seventeen = Node(17)
    thirteen = Node(13)
    three = Node(3)
    twenty_one = Node(21)
    thirty = Node(30)
    ten = Node(10)
    one = Node(1)
    five = Node(5)
  
    fifteen.left = two
    two.left = twenty
    twenty.right = seven
    two.right = thirty_one
    thirty_one.right = nine
    fifteen.right = seventeen
    seventeen.left = thirteen
    thirteen.left = three
    three.right = twenty_one
    seventeen.right = thirty
    thirty.left = ten
    ten.right = five
    ten.left = one

    arbor = BinaryTree()
    arbor.root = fifteen

    return arbor

def test_fixture_tree(tree):
    assert tree

def test_tree_traversal(tree):
    assert tree.root.left.value == 2
    assert tree.root.value == 15
    assert tree.root.right.right.left.value == 10

def test_fizzbuzz_number(tree):
    modified_tree = fizz_buzz_tree(tree)

    assert modified_tree.root.value == 'FizzBuzz'
    assert modified_tree.root.right.right.value == 'FizzBuzz'


def test_unmodded_number(tree):
    modified_tree = fizz_buzz_tree(tree)

    assert modified_tree.root.left.value == 2
    assert modified_tree.root.left.left.right.value == 7
    assert modified_tree.root.right.value == 17
    assert modified_tree.root.right.left.value == 13
    assert modified_tree.root.right.right.left.left.value == 1

def test_fizzes(tree):
    modified_tree = fizz_buzz_tree(tree)

    assert modified_tree.root.left.right.right.value == 'fizz'
    assert modified_tree.root.right.left.left.value == 'fizz'
    assert modified_tree.root.right.left.left.right.value == 'fizz'

def test_buzzes(tree):
    modified_tree = fizz_buzz_tree(tree)

    assert modified_tree.root.left.left.value == 'buzz'
    assert modified_tree.root.right.right.left.value == 'buzz'
    assert modified_tree.root.right.right.left.right.value == 'buzz'    



    


    