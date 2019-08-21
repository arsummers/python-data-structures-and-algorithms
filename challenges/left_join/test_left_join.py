import pytest
from hashtable import HashTable
from left_join import left_join

def test_exists():
    assert HashTable
    assert left_join

@pytest.fixture()
def left_table_synonyms():
    ht = HashTable()
    ht.add('fond', 'enamored')
    ht.add('wrath', 'anger')
    ht.add('diligent', 'employed')
    ht.add('outfit', 'clothes')
    ht.add('guide', 'usher')

    return ht

@pytest.fixture()
def right_table_antonyms():
    ht = HashTable()
    ht.add('fond', 'averse')
    ht.add('wrath', 'anger')
    ht.add('diligent', 'idle')
    ht.add('flow', 'jam')
    ht.add('guide', 'follow')

    return ht

def test_synonyms_table_get(left_table_synonyms):

    assert left_table_synonyms.get('fond') == 'enamored'
    assert left_table_synonyms.get('outfit') == 'clothes'

def test_synonyms_table_contains(left_table_synonyms):

    assert left_table_synonyms.contains('wrath')

def test_antonyms_table_get(right_table_antonyms):
    assert right_table_antonyms.get('fond') == 'averse'
    assert right_table_antonyms.get('flow') == 'jam'

def test_antonyms_table_contains(right_table_antonyms):
    assert right_table_antonyms.contains('guide')
