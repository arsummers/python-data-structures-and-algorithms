from tree import Node

def test_exists():
    assert Node

def test_has_value():
    n = Node('a')
    
    assert n.value == 'a'
    assert n.left == None
    assert n.right == None