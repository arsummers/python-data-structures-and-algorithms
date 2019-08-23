import pytest
from graph import Graph, Vertex

def test_exists():
    assert Graph
    assert Vertex

def test_add_single():
    g = Graph()
    ants = g.add_vertex('ants')
    assert isinstance(ants, Vertex)
    assert ants.value == 'ants'

def test_add_multiple():
    g = Graph()
    ants = g.add_vertex('ants')
    bats = g.add_vertex('bats')
    cats = g.add_vertex('cats')

    assert ants.value == 'ants'
    assert bats.value == 'bats'
    assert cats.value == 'cats'

def test_get_single():
    g = Graph()
    ants = g.add_vertex('ants')

    vertices = g.get_vertices()
    assert len(vertices) == 1
    assert vertices[0].value == 'ants'

def test_get_multiple():
    g = Graph()
    ants = g.add_vertex('ants')
    bats = g.add_vertex('bats')
    cats = g.add_vertex('cats')

    vertices = g.get_vertices()

    assert len(vertices) == 3
    assert {vertex.value for vertex in vertices} == set(['ants', 'bats', 'cats'])    

def test_length():
    g = Graph()
    ants = g.add_vertex('ants')
    bats = g.add_vertex('bats')
    cats = g.add_vertex('cats')

    assert len(g) == 3

def test_empty():
    g = Graph()

    assert g.get_vertices() == None


def test_add_edge():
    g = Graph()
    ants = g.add_vertex('ants')
    bats = g.add_vertex('bats')

    g.add_edge(ants, bats, 10)

    ants_bats_edge = ants.neighbors[0]

    assert ants_bats_edge.vertex == bats
    assert ants_bats_edge.weight == 10
    assert len(bats.neighbors) == 0

def test_get_neighbors():
    g = Graph()
    ants = g.add_vertex('ants')
    bats = g.add_vertex('bats')
    cats = g.add_vertex('cats')

    g.add_edge(ants, bats, 10)
    g.add_edge(ants, cats, 15)

    neighbors = g.get_neighbors(ants)

    assert neighbors[0].vertex.value == 'bats'
    assert neighbors[0].weight == 10

    assert neighbors[1].vertex.value == 'cats'
    assert neighbors[1].weight == 15

def test_self_loop():
    g = Graph()
    ants = g.add_vertex('ants')
    g.add_edge(ants, ants)

    neighbors = g.get_neighbors(ants)
    assert neighbors[0].vertex.value == 'ants'
    assert neighbors[0].weight == 0

    vertices = g.get_vertices()

    assert [vertex.value for vertex in vertices] == ['ants']



