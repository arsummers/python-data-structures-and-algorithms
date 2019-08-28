import pytest
from graph import Graph
from get_edge import get_edge

def test_exists():
    assert Graph
    assert get_edge


def test_graph_setup():
    g = Graph()

    aberdeen = g.add_vertex('Aberdeen')
    nairn = g.add_vertex('Nairn')
    perth = g.add_vertex('Perth')
    macduff = g.add_vertex('MacDuff')
    banff = g.add_vertex('Banff')
    glasgow = g.add_vertex('Glasgow')
    portree = g.add_vertex('Portree')

    g.add_edge(aberdeen, nairn, 70)
    g.add_edge(nairn, aberdeen, 70)
    g.add_edge(aberdeen, perth, 50)
    g.add_edge(perth, aberdeen, 50)
    g.add_edge(aberdeen, macduff, 35)
    g.add_edge(macduff, aberdeen, 35)
    g.add_edge(perth, macduff, 45)
    g.add_edge(macduff, perth, 45)
    g.add_edge(macduff, banff, 15)
    g.add_edge(banff, macduff, 15)
    g.add_edge(macduff, glasgow, 40)
    g.add_edge(glasgow, macduff, 40)

    aberdeen_neighbors = g.get_neighbors(aberdeen)
    nairn_neighbors = g.get_neighbors(nairn)
    macduff_neighbors = g.get_neighbors(macduff)
    glasgow_neighbors = g.get_neighbors(glasgow)

    assert aberdeen_neighbors[0].vertex.value == 'Nairn'    
    assert aberdeen_neighbors[1].vertex.value == 'Perth'
    assert aberdeen_neighbors[2].vertex.value == 'MacDuff'
    assert nairn_neighbors[0].vertex.value == 'Aberdeen'
    assert macduff_neighbors[0].vertex.value == 'Aberdeen'
    assert macduff_neighbors[1].vertex.value == 'Perth'
    assert macduff_neighbors[2].vertex.value == 'Banff'
    assert glasgow_neighbors[0].vertex.value == 'MacDuff'

@pytest.mark.skip()
def test_single_flight():
    g = Graph()

    aberdeen = g.add_vertex('Aberdeen')
    nairn = g.add_vertex('Nairn')
    perth = g.add_vertex('Perth')
    macduff = g.add_vertex('MacDuff')
    banff = g.add_vertex('Banff')
    glasgow = g.add_vertex('Glasgow')
    portree = g.add_vertex('Portree')

    g.add_edge(aberdeen, nairn, 70)
    g.add_edge(nairn, aberdeen, 70)
    g.add_edge(aberdeen, perth, 50)
    g.add_edge(perth, aberdeen, 50)
    g.add_edge(aberdeen, macduff, 35)
    g.add_edge(macduff, aberdeen, 35)
    g.add_edge(perth, macduff, 45)
    g.add_edge(macduff, perth, 45)
    g.add_edge(macduff, banff, 15)
    g.add_edge(banff, macduff, 15)
    g.add_edge(macduff, glasgow, 40)
    g.add_edge(glasgow, macduff, 40)

    assert get_edge(g, [aberdeen, nairn]) == True, f'${70}'

@pytest.mark.skip()
def test_double_flight():
    g = Graph()

    aberdeen = g.add_vertex('Aberdeen')
    nairn = g.add_vertex('Nairn')
    perth = g.add_vertex('Perth')
    macduff = g.add_vertex('MacDuff')
    banff = g.add_vertex('Banff')
    glasgow = g.add_vertex('Glasgow')
    portree = g.add_vertex('Portree')

    g.add_edge(aberdeen, nairn, 70)
    g.add_edge(nairn, aberdeen, 70)
    g.add_edge(aberdeen, perth, 50)
    g.add_edge(perth, aberdeen, 50)
    g.add_edge(aberdeen, macduff, 35)
    g.add_edge(macduff, aberdeen, 35)
    g.add_edge(perth, macduff, 45)
    g.add_edge(macduff, perth, 45)
    g.add_edge(macduff, banff, 15)
    g.add_edge(banff, macduff, 15)
    g.add_edge(macduff, glasgow, 40)
    g.add_edge(glasgow, macduff, 40)

    assert get_edge(g, [aberdeen, macduff, glasgow]) == True, f'${75}'


@pytest.mark.skip()
def test_for_false():
    g = Graph()

    aberdeen = g.add_vertex('Aberdeen')
    nairn = g.add_vertex('Nairn')
    perth = g.add_vertex('Perth')
    macduff = g.add_vertex('MacDuff')
    banff = g.add_vertex('Banff')
    glasgow = g.add_vertex('Glasgow')
    portree = g.add_vertex('Portree')

    g.add_edge(aberdeen, nairn, 70)
    g.add_edge(nairn, aberdeen, 70)
    g.add_edge(aberdeen, perth, 50)
    g.add_edge(perth, aberdeen, 50)
    g.add_edge(aberdeen, macduff, 35)
    g.add_edge(macduff, aberdeen, 35)
    g.add_edge(perth, macduff, 45)
    g.add_edge(macduff, perth, 45)
    g.add_edge(macduff, banff, 15)
    g.add_edge(banff, macduff, 15)
    g.add_edge(macduff, glasgow, 40)
    g.add_edge(glasgow, macduff, 40)

    assert get_edge(g, [perth, nairn]) == False, '$0'


@pytest.mark.skip()
def test_for_false_island():
    g = Graph()

    aberdeen = g.add_vertex('Aberdeen')
    nairn = g.add_vertex('Nairn')
    perth = g.add_vertex('Perth')
    macduff = g.add_vertex('MacDuff')
    banff = g.add_vertex('Banff')
    glasgow = g.add_vertex('Glasgow')
    portree = g.add_vertex('Portree')

    g.add_edge(aberdeen, nairn, 70)
    g.add_edge(nairn, aberdeen, 70)
    g.add_edge(aberdeen, perth, 50)
    g.add_edge(perth, aberdeen, 50)
    g.add_edge(aberdeen, macduff, 35)
    g.add_edge(macduff, aberdeen, 35)
    g.add_edge(perth, macduff, 45)
    g.add_edge(macduff, perth, 45)
    g.add_edge(macduff, banff, 15)
    g.add_edge(banff, macduff, 15)
    g.add_edge(macduff, glasgow, 40)
    g.add_edge(glasgow, macduff, 40)

    assert get_edge(g, [glasgow, portree]) == False, '$0'