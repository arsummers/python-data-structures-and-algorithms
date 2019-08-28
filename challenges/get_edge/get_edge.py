from graph import Graph
from collections import deque

def get_edge(graph, cities):

    q = deque()
    results = []
    price = 0

    for city in cities:
        q.appendleft(city)

    