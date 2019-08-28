from graph import Graph
from collections import deque

def get_edge(graph, cities):

    q = deque()
    price = 0
    for city in cities:
        q.appendleft(city)


    while q:
        current = q.pop()
        
        for edge in current.neighbors:
            tracker = 0
            for city in cities:
                tracker += 1

            # if next city.value in the queue matches the next item in the list of cities, I can bump up the price, return true and price
                if current == cities[tracker]:
                    return True, f'${price}'

                elif current != cities[tracker]:
                    return False, '$0'