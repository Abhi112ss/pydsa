METADATA = {
    "id": 824,
    "name": "Goat Latin",
    "slug": "goat_latin",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Convert a sentence to Goat Latin by moving consonants to the end, appending 'ma', and adding position-based trailing 'a's.",
}

def solve(sentence: str) -> str:
    """Convert a sentence to Goat Latin.

    Rules:
        - If a word begins with a vowel, append 'ma' to the end.
        - If a word begins with a consonant, move the first letter to the end, then append 'ma'.
        - Append one 'a' for the first word, two for the second, etc.

    Args:
        sentence: A string of words separated by single spaces.

    Returns:
        The sentence converted to Goat Latin.

    Examples:
        >>> solve("I speak Goat Latin")
        "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        >>> solve("The quick brown fox jumped over the lazy dog")
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    """
    vowels = set("aeiouAEIOU")
    words = sentence.split(" ")
    result_words = []

    for index, word in enumerate(words):
        # Determine suffix: 'ma' + (index+1) 'a's
        suffix = "ma" + "a" * (index + 1)

        if word[0] in vowels:
            # Vowel-starting word: just append suffix
            result_words.append(word + suffix)
        else:
            # Consonant-starting word: move first letter to end, then append suffix
            result_words.append(word[1:] + word[0] + suffix)

    return " ".join(result_words)