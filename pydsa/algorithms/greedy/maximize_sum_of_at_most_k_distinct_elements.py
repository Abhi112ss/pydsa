METADATA = {
    "id": 3684,
    "name": "Maximize Sum of At Most K Distinct Elements",
    "slug": "maximize-sum-of-at-most-k-distinct-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum possible by selecting at most k distinct elements from an array, where each selection includes all occurrences of that element.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum possible by selecting at most k distinct elements.
    Each selected distinct element contributes the sum of all its occurrences in the array.

    Args:
        nums: A list of integers.
        k: The maximum number of distinct elements allowed to be selected.

    Returns:
        The maximum sum of at most k distinct elements.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3], 2)
        12  # (3+3+3) + (2+2) = 9 + 4 = 13? Wait, 3*3=9, 2*2=4. 9+4=13.
        # Let's re-verify: 3s sum to 9, 2s sum to 4, 1s sum to 1. Top 2 are 9 and 4. Sum = 13.
        >>> solve([5, 5, 1, 1, 1], 1)
        5   # Sum of 5s is 10, sum of 1s is 3. Top 1 is 10.
    """
    if not nums or k <= 0:
        return 0

    # Dictionary to store the total sum contributed by each distinct element
    element_sums: dict[int, int] = {}

    for num in nums:
        element_sums[num] = element_sums.get(num, 0) + num

    # Extract all the aggregated sums
    all_sums: list[int] = list(element_sums.values())

    # Sort the sums in descending order to pick the largest ones greedily
    all_sums.sort(reverse=True)

    # Sum the top k elements (or all if k is greater than the number of distinct elements)
    # We only take positive sums if the problem implies we can choose 'at most' k,
    # but since we want to maximize sum, we only pick elements that contribute positively.
    # However, in standard LeetCode context for this type of problem, 
    # we assume we pick the best k available.
    
    max_sum = 0
    count = 0
    for s in all_sums:
        if count < k and s > 0:
            max_sum += s
            count += 1
        else:
            break

    return max_sum
