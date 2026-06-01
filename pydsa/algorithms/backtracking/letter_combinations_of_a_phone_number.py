METADATA = {
    "id": 17,
    "name": "Letter Combinations of a Phone Number",
    "slug": "letter-combinations-of-a-phone-number",
    "category": "String",
    "aliases": [],
    "tags": ["backtracking", "string", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(4^n)",
    "space_complexity": "O(n)",
    "description": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.",
}

def solve(digits: str) -> list[str]:
    """
    Generates all possible letter combinations for a given string of digits.

    Args:
        digits: A string containing digits from 2-9.

    Returns:
        A list of strings representing all possible letter combinations.

    Examples:
        >>> solve("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> solve("")
        []
    """
    if not digits:
        return []

    # Mapping of digits to their corresponding letters on a phone keypad
    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    combinations: list[str] = []

    def backtrack(index: int, current_path: list[str]) -> None:
        """
        A recursive helper function to explore all combinations using backtracking.

        Args:
            index: The current digit index we are processing.
            current_path: A list of characters representing the combination built so far.
        """
        # Base case: if the current path length equals the input digits length, we found a combination
        if index == len(digits):
            combinations.append("".join(current_path))
            return

        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        letters = digit_to_letters[current_digit]

        # Iterate through each letter and move to the next digit
        for letter in letters:
            current_path.append(letter)
            backtrack(index + 1, current_path)
            # Backtrack: remove the last letter to try the next possibility
            current_path.pop()

    backtrack(0, [])
    return combinations
