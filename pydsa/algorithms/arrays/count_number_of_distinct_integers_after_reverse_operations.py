METADATA = {
    "id": 2442,
    "name": "Count Number of Distinct Integers After Reverse Operations",
    "slug": "count-number-of-distinct-integers-after-reverse-operations",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n * log10(max_val))",
    "space_complexity": "O(n)",
    "description": "Count the number of unique integers in a list after adding the reverse of each integer to the collection.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of distinct integers after performing reverse operations on each element.

    Args:
        nums: A list of integers.

    Returns:
        The count of unique integers present in the combined set of original and reversed numbers.

    Examples:
        >>> solve([1, 13, 10, 5])
        5
        >>> solve([5, 5, 5, 5])
        1
    """
    # Use a set to automatically handle uniqueness
    distinct_elements = set()

    for number in nums:
        # Add the original number to the set
        distinct_elements.add(number)
        
        # Reverse the digits of the current number
        # We convert to string to easily reverse, then back to int to handle leading zeros
        reversed_number = int(str(number)[::-1])
        
        # Add the reversed number to the set
        distinct_elements.add(reversed_number)

    return len(distinct_elements)
