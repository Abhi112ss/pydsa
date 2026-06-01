METADATA = {
    "id": 740,
    "name": "Delete and Earn",
    "slug": "delete-and-earn",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n + max_val)",
    "space_complexity": "O(max_val)",
    "description": "Maximize points by picking numbers such that picking a number prevents picking its neighbors (x-1 and x+1).",
}

def solve(nums: list[int]) -> int:
    """
    Solves the Delete and Earn problem by transforming it into a House Robber problem.

    The core idea is to create a frequency array where the index represents the number
    and the value at that index represents the total points obtainable from that number.
    Once transformed, the problem becomes: "Select elements from the array such that
    no two adjacent elements are chosen," which is the classic House Robber problem.

    Args:
        nums: A list of integers representing the points available.

    Returns:
        The maximum points that can be earned.

    Examples:
        >>> solve([3, 4, 2])
        6
        >>> solve([2, 2, 3, 3, 3, 4])
        9
        >>> solve([3, 4, 5])
        8
    """
    if not nums:
        return 0

    # Find the range of numbers to build the frequency-weighted array
    max_val = max(nums)
    
    # points_at[i] will store the total sum of all occurrences of number 'i'
    # This transforms the problem into: "If I pick i, I get points_at[i] but cannot pick points_at[i-1] or points_at[i+1]"
    points_at = [0] * (max_val + 1)
    for num in nums:
        points_at[num] += num

    # Standard House Robber DP approach
    # prev_max: maximum points earned up to the previous index (i-1)
    # curr_max: maximum points earned up to the current index (i)
    prev_max = 0
    curr_max = 0

    for points in points_at:
        # At each step, we decide:
        # 1. Skip the current number: total points remains curr_max
        # 2. Take the current number: total points is prev_max + points (from index i-2)
        new_max = max(curr_max, prev_max + points)
        prev_max = curr_max
        curr_max = new_max

    return curr_max
