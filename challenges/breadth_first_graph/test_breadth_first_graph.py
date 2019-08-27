import pytest
from breadth_first_graph import Graph

@pytest.fixture()
def graph():
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


    return graf