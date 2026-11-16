import pytest
from exercises.algorithms import (is_even, are_anagrams, character_frequency,
    fibonacci, non_repeating_characters, first_non_repeating_character,
    substrings, is_prime, reverse_string)


@pytest.mark.parametrize("value,expected", [(0,True),(2,True),(-3,False),(7,False)])
def test_even(value, expected):
    assert is_even(value) is expected


@pytest.mark.parametrize("first,second,expected", [("listen","silent",True),("aab","abb",False),("","",True),("A","a",False)])
def test_anagrams(first, second, expected):
    assert are_anagrams(first, second) is expected


def test_character_frequency():
    assert character_frequency("hello") == {"h":1,"e":1,"l":2,"o":1}
    assert character_frequency("") == {}


@pytest.mark.parametrize("count,expected", [(0,[]),(1,[0]),(2,[0,1]),(7,[0,1,1,2,3,5,8])])
def test_fibonacci(count, expected):
    assert fibonacci(count) == expected


def test_negative_fibonacci_count():
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.parametrize("text,unique,first", [("helloh",["e","o"],"e"),("aabb",[],None),("",[],None),("swiss",["w","i"],"w")])
def test_non_repeating(text, unique, first):
    assert non_repeating_characters(text) == unique
    assert first_non_repeating_character(text) == first


def test_substrings():
    assert substrings("abc") == ["a","ab","abc","b","bc","c"]
    assert substrings("aa") == ["a","aa","a"]
    assert substrings("") == []


@pytest.mark.parametrize("value,expected", [(-5,False),(0,False),(1,False),(2,True),(3,True),(4,False),(25,False),(97,True)])
def test_primes(value, expected):
    assert is_prime(value) is expected


@pytest.mark.parametrize("text,expected", [("Vinay","yaniV"),("",""),(" a","a ")])
def test_reverse(text, expected):
    assert reverse_string(text) == expected
