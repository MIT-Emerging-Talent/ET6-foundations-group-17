# mirror_words_challenge
"""
This module provides a function to reverse each word in a sentence
while keeping the order of the words intact.

Module contents:
    - reverse_words: returns a new string where each word is reversed, 
      but the order of the words and punctuation remains unchanged.

Created on 2025-01-05
@author: Aseel A. S. AbuKmail
"""

def reverse_words(sentence: str) -> str:
    """Returns a new string where each word is reversed while preserving the word order.

    The function should:
    - Accept a single string as input.
    - Reverse each word in the sentence while keeping the order of the words intact.
    - Maintain all spaces and punctuation exactly as they appear.

    Parameter:
    sentence: a string containing words to be reversed.

    Returns -> str: a new string where each word is reversed, 
                     but the order of the words and spaces is preserved.

    Examples:
        >>> reverse_words("Hello world!")
        'olleH dlrow!'

        >>> reverse_words("Python is fun.")
        'nohtyP si .nuf'

        >>> reverse_words("Keep calm and code on.")
        'peeK mlac dna edoc .no'
    """
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word and join them back with spaces
    reversed_words = " ".join(word[::-1] for word in words)
    return reversed_words
