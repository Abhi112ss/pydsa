METADATA = {
    "id": 273,
    "name": "Integer to English Words",
    "slug": "integer-to-english-words",
    "category": "Math",
    "aliases": [],
    "tags": ["recursion", "math", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Convert a non-negative integer to its English words representation.",
}

def solve(num: int) -> str:
    """
    Converts a non-negative integer into its English words representation.

    Args:
        num: A non-negative integer.

    Returns:
        A string representing the English words for the given number.

    Examples:
        >>> solve(12345)
        'Twelve Thousand Three Hundred Forty Five'
        >>> solve(1234567)
        'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'
    """
    if num == 0:
        return "Zero"

    # Mapping of numbers to their English words
    LESS_THAN_20 = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    TENS = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def helper(n: int) -> list[str]:
        """Recursive helper to process numbers in chunks of three digits."""
        if n == 0:
            return []
        elif n < 20:
            return [LESS_THAN_20[n]]
        elif n < 100:
            # Handle tens place and remainder
            remainder = n % 10
            if remainder == 0:
                return [TENS[n // 10]]
            else:
                return [TENS[n // 10], *helper(remainder)]
        else:
            # Handle hundreds place and remainder
            remainder = n % 100
            if remainder == 0:
                return [LESS_THAN_20[n // 100], "Hundred"]
            else:
                return [LESS_THAN_20[n // 100], "Hundred", *helper(remainder)]

    result_parts: list[str] = []
    thousand_idx = 0

    # Process the number in chunks of 1000
    while num > 0:
        if num % 1000 != 0:
            # Get words for the current 3-digit chunk
            chunk_words = helper(num % 1000)
            # Append the scale (Thousand, Million, etc.) if applicable
            if THOUSANDS[thousand_idx]:
                chunk_words.append(THOUSANDS[thousand_idx])
            
            # Prepend the chunk words to the result list
            # We use slicing/addition to maintain order of magnitude
            result_parts = chunk_words + result_parts
            
        num //= 1000
        thousand_idx += 1

    return " ".join(result_parts)
