METADATA = {
    "id": 2042,
    "name": "Check if Numbers Are Ascending in a Sentence",
    "slug": "check-if-numbers-are-ascending-in-a-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string", "parsing"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Check if all numbers appearing in a sentence are in strictly increasing order.",
}

def solve(sentence: str) -> bool:
    """
    Checks if the numbers appearing in a sentence are in strictly increasing order.

    Args:
        sentence: A string containing words and numbers separated by spaces.

    Returns:
        True if all numbers are strictly increasing, False otherwise.

    Examples:
        >>> solve("say 34 12 3")
        False
        >>> solve("one way to 2 3 4")
        True
        >>> solve("1 2 3")
        True
    """
    words = sentence.split()
    previous_number = float('-inf')

    for word in words:
        # Check if the current word consists only of digits
        if word.isdigit():
            current_number = int(word)
            
            # If the current number is not strictly greater than the previous, return False
            if current_number <= previous_number:
                return False
            
            # Update the tracker for the next comparison
            previous_number = current_number

    return True
