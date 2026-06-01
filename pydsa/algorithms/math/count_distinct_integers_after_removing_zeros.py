METADATA = {
    "id": 3747,
    "name": "Count Distinct Integers After Removing Zeros",
    "slug": "count-distinct-integers-after-removing-zeros",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n)",
    "description": "Count the number of distinct integers remaining after removing all zeros from each integer in a given list.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of distinct integers formed by removing all zeros from each number.

    Args:
        nums: A list of integers.

    Returns:
        The count of unique integers remaining after zero removal.

    Examples:
        >>> solve([102, 304, 102])
        2
        >>> solve([1, 0, 2, 0, 3])
        3
        >>> solve([100, 200, 300])
        3
    """
    distinct_integers = set()

    for number in nums:
        # Convert number to string to manipulate digits
        num_str = str(number)
        
        # Remove all occurrences of '0'
        # Note: If the number was '0', it becomes an empty string
        # However, the problem context implies we are removing zeros from existing digits.
        # If a number becomes empty (e.g., '0' -> ''), we skip it or handle as per logic.
        # Based on standard LeetCode interpretation for this type of problem:
        # We treat the resulting digits as a new integer.
        stripped_str = num_str.replace("0", "")
        
        if stripped_str:
            # Convert back to int to ensure uniqueness (e.g., "01" and "1" are both 1)
            # and add to the set.
            distinct_integers.add(int(stripped_str))
            
    return len(distinct_integers)
