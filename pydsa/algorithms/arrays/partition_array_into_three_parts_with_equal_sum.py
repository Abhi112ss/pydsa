METADATA = {
    "id": 1013,
    "name": "Partition Array Into Three Parts With Equal Sum",
    "slug": "partition-array-into-three-parts-with-equal-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can be partitioned into three non-empty contiguous parts with equal sums.",
}

def solve(arr: list[int]) -> bool:
    """
    Determines if the array can be partitioned into three non-empty parts with equal sums.

    Args:
        arr: A list of integers.

    Returns:
        True if the array can be partitioned into three parts with equal sum, False otherwise.

    Examples:
        >>> solve([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
        True
        >>> solve([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1, 1])
        False
        >>> solve([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
        False
    """
    total_sum = sum(arr)

    # If the total sum is not divisible by 3, we cannot partition it into 3 equal parts.
    if total_sum % 3 != 0:
        return False

    target_sum = total_sum // 3
    current_running_sum = 0
    parts_found = 0
    n = len(arr)

    # Iterate through the array to find segments that sum up to the target_sum.
    # We only need to find the first two parts; if we find two parts and there is 
    # remaining elements, the third part must automatically sum to the target.
    for i in range(n):
        current_running_sum += arr[i]
        
        if current_running_sum == target_sum:
            parts_found += 1
            current_running_sum = 0
            
            # If we have found 2 parts, we must ensure there is at least one 
            # element left to form the 3rd part.
            if parts_found == 2 and i < n - 1:
                return True

    return False
