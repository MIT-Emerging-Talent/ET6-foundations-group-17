import re


def mirror_words(sentence: str) -> str:
    """
    Reverses each word in a given sentence while maintaining the order of the words.
    Punctuation marks at the end of words are correctly handled, ensuring they remain
    in place.

    Args:
        sentence (str): The sentence to be processed. It can contain words, punctuation,
        spaces, numbers, and special characters.
    Returns:
        str: A new string where each word is reversed, but the word order, punctuation,
        numbers, and special characters remain unchanged.

    Example:
        >>> mirror_words("Hello world!")
        'olleH dlrow!'

        >>> mirror_words("Python is fun")
        'nohtyP si nuf'

        >>> mirror_words("Keep calm & code on.")
        'peeK mlac & edoc .no'

    Raises:
        TypeError: If the input is not a string.

    Note:
    This function processes each word individually, reversing only the characters
    in the word while leaving punctuation, numbers, and special characters
    unchanged.

    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    # Split the sentence into words
    words = sentence.split()

    mirrored_words_list = []  # List to store the mirrored words
    for word in words:
        # Match the word and any punctuation at the end
        match = re.match(r"([a-zA-Z]+)([^a-zA-Z]*)", word)
        if match:
            # Reverse the word and keep punctuation at the end without reversing it
            mirrored_words_list.append(match.group(1)[::-1] + match.group(2))
        else:
            mirrored_words_list.append(word)

    return " ".join(mirrored_words_list)
