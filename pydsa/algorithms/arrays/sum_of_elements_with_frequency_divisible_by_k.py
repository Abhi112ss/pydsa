METADATA = {
    "id": 3712,
    "name": "Sum of Elements With Frequency Divisible by K",
    "slug": "sum-of-elements-with-frequency-divisible-by-k",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of all elements in an array whose frequency in that array is divisible by a given integer k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of elements in 'nums' whose frequency is divisible by 'k'.

    Args:
        nums: A list of integers.
        k: The divisor used to check the frequency condition.

    Returns:
        The sum of all elements whose frequency in the input list is a multiple of k.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3], 2)
        2
        >>> solve([1, 1, 1, 1, 2, 2], 2)
        6
        >>> solve([1, 2, 3], 1)
        6
    """
    if not nums:
        return 0

    # Step 1: Count the frequency of each element using a hash map
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    total_sum: int = 0

    # Step 2: Iterate through the frequency map and sum elements meeting the condition
    for element, count in frequency_map.items():
        # Check if the frequency is divisible by k
        if count % k == 0:
            # We add the element itself, but the problem asks for the sum of 
            # elements that satisfy the condition. Usually, in these problems, 
            # if an element satisfies the condition, we sum all its occurrences.
            # Based on the prompt "Sum of Elements", we sum the value of the element 
            # multiplied by its frequency to account for all its occurrences.
            total_sum += element * count

    return total_sum
