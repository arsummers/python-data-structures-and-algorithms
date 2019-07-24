import pytest
from multi_bracket_validation import multi_bracket_validation

def test_m_b_v_exists():
    assert multi_bracket_validation

def test_two_curlies():
    expected = True
    actual = multi_bracket_validation('{}')

    assert expected == actual

def test_three_pairs():
    expected = True
    actual = multi_bracket_validation('{}(){}')

    assert expected == actual   

def test_consec_with_words():
    expected = True
    actual = multi_bracket_validation('()[[Extra Characters]]')

    assert expected == actual

def test_funky_mirror():
    expected = True
    actual = multi_bracket_validation('(){}[[]]')

    assert expected == actual

def test_nonconsec_words():
    expected = True
    actual = multi_bracket_validation('{}{Code}[Fellows](())')

    assert expected == actual


def test_odd_some_matches():
    expected = False
    actual = multi_bracket_validation('[({}]')

    assert expected == actual

def test_odd_no_matches():
    expected = False
    actual = multi_bracket_validation('(](')

    assert expected == actual

def test_even_no_mirror():
    expected = False
    actual = multi_bracket_validation('{(})')

    assert expected == actual

def test_single_open_bracket():
    expected = False
    actual = multi_bracket_validation('{')

    assert expected == actual

def test_single_close_bracket():
    expected = False
    actual = multi_bracket_validation(']')

    assert expected == actual

def test_two_mismatch():
    expected = False
    actual = multi_bracket_validation('[}')

    assert expected == actual