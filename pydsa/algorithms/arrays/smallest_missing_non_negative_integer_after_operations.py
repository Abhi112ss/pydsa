METADATA = {
    "id": 2598,
    "name": "Smallest Missing Non-negative Integer After Operations",
    "slug": "smallest-missing-non-negative-integer-after-operations",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest non-negative integer that does not appear in the array after applying modulo operations to all elements.",
}

def solve(nums: list[int], x: int) -> int:
    """
    Finds the smallest non-negative integer not present in the array after 
    applying the operation nums[i] % x to every element.

    Args:
        nums: A list of integers.
        x: The divisor for the modulo operation.

    Returns:
        The smallest non-negative integer not in the modified array.

    Examples:
        >>> solve([1, 2, 3], 2)
        0
        >>> solve([0, 1, 2], 3)
        3
        >>> solve([10, 12, 15], 5)
        1
    """
    # Use a set for O(1) average time complexity lookups
    seen_remainders = set()

    # Apply the modulo operation to each element and store in the set
    for num in nums:
        seen_remainders.add(num % x)

    # Iterate starting from 0 to find the first integer not in the set
    # The maximum possible answer is n (if all numbers 0 to n-1 are present)
    current_candidate = 0
    while current_candidate in seen_remainders:
        current_candidate += 1

    return current_candidate
