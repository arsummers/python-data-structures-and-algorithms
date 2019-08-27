import pytest
from breadth_first_graph import Graph, Vertex

def test_exists():
    assert Graph

def test_setup():
    graf = Graph()
    a = graf.add_vertex('a')
    b = graf.add_vertex('b')
    c = graf.add_vertex('c')
    d = graf.add_vertex('d')
    e = graf.add_vertex('e')
    f = graf.add_vertex('f')
    g = graf.add_vertex('g')

    graf.add_edge(a, c)
    graf.add_edge(a, b)

    graf.add_edge(c, d)
    graf.add_edge(c, e)

    graf.add_edge(b, f)

    graf.add_edge(f, g)
    graf.add_edge(d, g)

    a_neighbors = graf.get_neighbors(a)
    c_neighbors = graf.get_neighbors(c)
    b_neighbors = graf.get_neighbors(b)
    d_neighbors = graf.get_neighbors(d)
    f_neighbors = graf.get_neighbors(f)


    # cannot assert for None  edges with list data structure
    assert a_neighbors[0].vertex.value == 'c'
    assert a_neighbors[1].vertex.value == 'b'
    assert b_neighbors[0].vertex.value == 'f'
    assert c_neighbors[0].vertex.value == 'd'
    assert c_neighbors[1].vertex.value == 'e'
    assert d_neighbors[0].vertex.value == 'g'
    assert f_neighbors[0].vertex.value == 'g'

@pytest.mark.skip()
def test_breadth_first():
    graf = Graph()
    a = graf.add_vertex('a')
    b = graf.add_vertex('b')
    c = graf.add_vertex('c')
    d = graf.add_vertex('d')
    e = graf.add_vertex('e')
    f = graf.add_vertex('f')
    g = graf.add_vertex('g')

    graf.add_edge(a, c)
    graf.add_edge(a, b)

    graf.add_edge(c, d)
    graf.add_edge(c, e)

    graf.add_edge(b, f)

    graf.add_edge(f, g)
    graf.add_edge(d, g)    

    expected = ['a', 'c', 'b', 'e', 'd', 'f', 'g']
    actual = graf.breadth_first(a)

    assert expected == actual