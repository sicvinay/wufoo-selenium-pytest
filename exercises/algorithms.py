"""Pure functions refactored from the bundled Python practice scripts."""
from collections import Counter
from math import isqrt


def is_even(number):
    return number % 2 == 0


def are_anagrams(first, second):
    """Case-sensitive; spaces and punctuation count."""
    return Counter(first) == Counter(second)


def character_frequency(text):
    return dict(Counter(text))


def fibonacci(count):
    """Exactly count terms starting with 0, 1."""
    if count < 0:
        raise ValueError("count cannot be negative")
    result = []
    first, second = 0, 1
    for _ in range(count):
        result.append(first)
        first, second = second, first + second
    return result


def non_repeating_characters(text):
    counts = Counter(text)
    return [char for char in text if counts[char] == 1]


def first_non_repeating_character(text):
    counts = Counter(text)
    return next((char for char in text if counts[char] == 1), None)


def substrings(text):
    """Non-empty contiguous substrings, retaining repeated occurrences."""
    return [text[start:end] for start in range(len(text))
            for end in range(start + 1, len(text) + 1)]


def is_prime(number):
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, isqrt(number) + 1))


def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result
