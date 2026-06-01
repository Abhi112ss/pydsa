METADATA = {
    "id": 3758,
    "name": "Convert Number Words to Digits",
    "slug": "convert-number-words-to-digits",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Convert a space-separated string of number words into their corresponding integer sum.",
}

def solve(s: str) -> int:
    """
    Converts a string of number words into their integer sum.

    Args:
        s: A space-separated string containing words representing digits.

    Returns:
        The sum of the digits represented by the words.

    Examples:
        >>> solve("one two three")
        6
        >>> solve("zero zero five")
        5
        >>> solve("nine")
        9
    """
    # Mapping of number words to their integer values
    word_to_digit = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    total_sum = 0
    
    # Split the input string by whitespace to iterate through each word
    words = s.split()

    for word in words:
        # Retrieve the digit value from the map and add to the running total
        # We assume the input is valid per problem constraints
        total_sum += word_to_digit[word]

    return total_sum
