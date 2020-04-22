import pytest
from cloud_jumping import cloud_jumping

def test_exists():
    assert cloud_jumping

def test_only_jump_thunder():
    c = [0, 0, 1, 0, 0, 1, 0]
    actual = cloud_jumping(c)
    expected = 4
    assert expected == actual

def test_jump_some_clouds():
    c = [0, 0, 0, 0, 1, 0]
    actual = cloud_jumping(c)
    expected = 3
    assert expected == actual

def test_alternating_thunder():
    c = [0, 1, 0, 1, 0, 1, 0]
    actual = cloud_jumping(c)
    expected = 3
    assert expected == actual

def test_no_thunder_odd():
    c = [0, 0, 0, 0, 0, 0, 0]
    actual = cloud_jumping(c)
    expected = 3
    assert expected == actual

def test_no_thunder_even():
    c = [0, 0, 0, 0, 0, 0]
    actual = cloud_jumping(c)
    expected = 3
    assert expected == actual

def test_short_route():
    c = [0, 0]
    actual = cloud_jumping(c)
    expected = 1
    assert expected == actual

def test_other_short_route():
    c = [0, 1, 0]
    actual = cloud_jumping(c)
    expected = 1
    assert expected == actual