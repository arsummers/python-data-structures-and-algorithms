import pytest
from kickback_mini import *

def test_loop():
    dictionary = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

    assert loop(dictionary) == ['Wallstreet','Gambler','Parents']

def test_comprehension():
    dictionary = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

    assert comprehension(dictionary) == ['Wallstreet','Gambler','Parents']

def test_map():
    dictionary = [{'name': 'Wallstreet', 'average_spend': 82.01}, {'name': 'Gambler', 'average_spend': 107.00}, {'name': 'Parents', 'average_spend': 10.52}]

    assert map_(dictionary) == ['Wallstreet','Gambler','Parents']

