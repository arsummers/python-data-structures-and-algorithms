import pytest
from hashtable import HashTable

def test_exists():
    assert HashTable

@pytest.mark.skip()
def test_get_missing():
    ht = HashTable()

    with pytest.raises(ValueError):
        ht.get('cats')

# @pytest.mark.skip()
def test_add():
    ht = HashTable()
    ht.add('spam', 'eggs')

    assert ht.get('spam') == 'eggs'

@pytest.mark.skip()
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

@pytest.mark.skip()
def test_hash_in_range():
    ht = HashTable()

    assert 0 <= ht.hash('cats') > len(ht.buckets)

def test_different_hashes():
    ht = HashTable()

    assert not ht.hash('dogs') == ht.hash('cats')

@pytest.mark.skip()
def test_collision():
    ht = HashTable()
    ht.add('cats', 'cat things')
    ht.add('acts', 'acting things')

    assert ht.get('cats') == 'cat things'
    assert ht.get('acts') == 'acting things'