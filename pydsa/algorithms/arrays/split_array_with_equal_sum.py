METADATA = {
    "id": 548,
    "name": "Split Array with Equal Sum",
    "slug": "split_array_with_equal_sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_set", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find three indices such that the array is split into four non-empty parts with equal sums.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds three indices i, j, k such that the sums of the four resulting 
    subarrays are equal.

    The subarrays are defined as:
    - nums[0...i-1]
    - nums[i...j-1]
    - nums[j...k-1]
    - nums[k...n-1]

    Args:
        nums: A list of integers.

    Returns:
        A list of three integers [i, j, k] representing the split points.
        Returns an empty list if no such indices exist.

    Examples:
        >>> solve([1, 2, 3, 4, 4, 3, 2, 1])
        [2, 4, 6]
        >>> solve([1, 1, 1, 1])
        [1, 2, 3]
    """
    n = len(nums)
    if n < 4:
        return []

    # Precompute prefix sums to allow O(1) range sum calculation
    prefix_sums = [0] * (n + 1)
    for idx in range(n):
        prefix_sums[idx + 1] = prefix_sums[idx] + nums[idx]

    def get_sum(start: int, end: int) -> int:
        """Returns the sum of nums[start...end-1] using prefix sums."""
        return prefix_sums[end] - prefix_sums[start]

    # Iterate through all possible middle split points 'j'
    # j must leave at least 2 elements to the left (for i) and 2 to the right (for k)
    for j in range(2, n - 1):
        # left_sums stores the sums of the first subarray [0...i-1]
        # where the second subarray [i...j-1] has the same sum.
        # We use a set for O(1) lookup of valid 'i' values.
        left_sums = set()
        
        # Try to find a valid 'i' for the current 'j'
        # i must be at least 1 and at most j-1
        for i in range(1, j):
            sum_part1 = prefix_sums[i]
            sum_part2 = get_sum(i, j)
            if sum_part1 == sum_part2:
                left_sums.add(sum_part1)

        # Now try to find a valid 'k' for the current 'j'
        # k must be at least j+1 and at most n-1
        for k in range(j + 1, n):
            sum_part3 = get_sum(j, k)
            sum_part4 = get_sum(k, n)
            
            # If the two right parts are equal, check if that sum 
            # was achieved by valid left parts
            if sum_part3 == sum_part4 and sum_part3 in left_sums:
                # To return the actual indices, we need to find which 'i' worked.
                # Since the problem asks for any valid [i, j, k], we re-scan 
                # or we could have stored the index in the set.
                # For efficiency in this specific implementation, we re-scan i.
                for i_candidate in range(1, j):
                    if prefix_sums[i_candidate] == sum_part3 and get_sum(i_candidate, j) == sum_part3:
                        return [i_candidate, j, k]

    return []
