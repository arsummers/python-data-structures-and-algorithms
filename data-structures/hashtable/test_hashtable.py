import pytest
from hashtable import HashTable

def test_exists():
    assert HashTable

def test_get_missing():
    ht = HashTable()

    with pytest.raises(ValueError):
        ht.get('cats')
        
def test_add():
    ht = HashTable()
    ht.add('spam', 'eggs')

    assert ht.get('spam') == 'eggs'

def test_add_twice():
    ht = HashTable()
    ht.add('spam', 'eggs')
    ht.add('things', 'stuff')


    assert ht.get('spam') == 'eggs'
    assert ht.get('things') == 'stuff'

def test_contains():
    ht = HashTable()
    ht.add('spam', 'eggs')

    assert ht.contains('spam')

def test_not_contains():
    ht = HashTable()

    assert not ht.contains('spam')


def test_hash_same():
    ht = HashTable()

    assert ht.hash('dogs') == ht.hash('gods')

def test_hash_in_range():
    ht = HashTable()

    assert 0 <= ht.hash('cats') < len(ht.buckets)

def test_different_hashes():
    ht = HashTable()

    assert not ht.hash('dogs') == ht.hash('cats')


def test_collision():
    ht = HashTable()
    ht.add('cats', 'cat things')
    ht.add('acts', 'acting things')
    new_cats = ht.get('cats')
    new_acts = ht.get('acts')

    assert new_cats == 'cat things'
    assert new_acts == 'acting things'


# These are the tests I added on my own. Don't have them passing yet, but I do have some questions
@pytest.mark.skip()
def test_contains_with_collision():
    ht = HashTable()
    ht.add('spam', 'eggs')
    ht.add('maps', 'stuff')

    assert ht.contains('spam')
    assert ht.contains('maps')


@pytest.mark.skip()
def test_contains_multiple():
    ht = HashTable()
    ht.add('spam', 'eggs')
    ht.add('things', 'stuff')

    assert ht.contains('spam')
    assert ht.contains('maps')