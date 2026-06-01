METADATA = {
    "id": 3737,
    "name": "Count Subarrays With Majority Element I",
    "slug": "count-subarrays-with-majority-element-i",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where a specific target element appears more than half the time.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Counts the number of subarrays where the target element is the majority element.
    
    A majority element in a subarray of length L is an element that appears 
    more than L // 2 times. This is equivalent to saying the count of 
    target elements is strictly greater than the count of non-target elements.

    Args:
        nums: A list of integers.
        target: The integer to check for majority status.

    Returns:
        The total count of subarrays where 'target' is the majority element.

    Examples:
        >>> solve([1, 2, 1, 3, 1], 1)
        6
        >>> solve([1, 1, 2, 2], 1)
        2
    """
    # Transform the problem: 
    # Let target be +1 and any other element be -1.
    # A subarray has target as majority if sum(transformed_subarray) > 0.
    
    count = 0
    current_prefix_sum = 0
    
    # We need to count pairs (i, j) such that prefix_sum[j] - prefix_sum[i] > 0
    # where j > i. This is equivalent to prefix_sum[j] > prefix_sum[i].
    # Since prefix sums change by exactly +1 or -1, we can use a Fenwick tree 
    # or a frequency map with a running count to solve this in O(n).
    
    # However, for a simpler O(n) approach with prefix sums:
    # We track the frequency of each prefix sum encountered so far.
    # To handle the 'greater than' condition efficiently, we use a Fenwick tree 
    # (Binary Indexed Tree) to count how many previous prefix sums are less than 
    # the current prefix sum.
    
    # Offset to handle negative indices in Fenwick tree
    # Max possible sum is n, min is -n. Range is 2n + 1.
    n = len(nums)
    offset = n + 1
    bit = [0] * (2 * n + 5)

    def update(idx: int, val: int):
        idx += offset
        while idx < len(bit):
            bit[idx] += val
            idx += idx & (-idx)

    def query(idx: int) -> int:
        idx += offset
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    # Initial state: prefix sum 0 has occurred once
    update(0, 1)
    
    for x in nums:
        # Update current prefix sum
        if x == target:
            current_prefix_sum += 1
        else:
            current_prefix_sum -= 1
        
        # We want to find how many previous prefix_sums < current_prefix_sum
        # query(current_prefix_sum - 1) gives count of sums in range [-n, current_prefix_sum - 1]
        count += query(current_prefix_sum - 1)
        
        # Add current prefix sum to the BIT
        update(current_prefix_sum, 1)
        
    return count
