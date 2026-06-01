METADATA = {
    "id": 2640,
    "name": "Find the Score of All Prefixes of an Array",
    "slug": "find-the-score-of-all-prefixes-of-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the score of each prefix of an array, where the score is the sum of elements in the prefix.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Calculates the score of all prefixes of the given array.
    The score of a prefix is defined as the sum of all elements in that prefix.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where the i-th element is the sum of the first i+1 elements of nums.

    Examples:
        >>> solve([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> solve([10, -5, 2, 1])
        [10, 5, 7, 8]
    """
    n = len(nums)
    prefix_scores = []
    current_running_sum = 0

    for num in nums:
        # Update the running sum by adding the current element
        current_running_sum += num
        # Append the current sum to the result list to represent the prefix score
        prefix_scores.append(current_running_sum)

    return prefix_scores
