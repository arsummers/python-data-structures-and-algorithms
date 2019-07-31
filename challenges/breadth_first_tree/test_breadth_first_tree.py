import pytest
from breadth_first_tree import BinaryTree, Node

def test_exists():
    assert BinaryTree
    assert Node

@pytest.fixture()
def tree():
    one =  Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

  
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven


    arbor = BinaryTree()
    arbor.root = one

    return arbor

def test_fixture_tree(tree):
    assert tree


@pytest.mark.skip('unsure how to modify test')
def test_prints(capsys):
    
    results.breadth_first()

    out = capsys.readouterr()

    assert out.out == 'print 1\nprint 2\n'

@pytest.mark.skip('unsure how to modify test')
def test_results_list(tree):
    assert results == [1, 2, 3, 4, 5, 6, 7]

