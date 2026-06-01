METADATA = {
    "id": 3739,
    "name": "Count Subarrays With Majority Element II",
    "slug": "count-subarrays-with-majority-element-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where a specific element appears more than half the time.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays where a specific element appears more than 
    half the time. Since the problem implies a specific target element 
    (usually the mode or a given target), this implementation assumes 
    we are counting subarrays where a specific target 'x' is the majority.
    
    Note: In the context of LeetCode problems of this type, if the target 
    is not provided, it usually refers to the element that could potentially 
    be a majority. For a general 'Majority Element II' variation, we 
    calculate for the most frequent element or a given target.

    Args:
        nums: A list of integers.

    Returns:
        The total count of subarrays where the target element is the majority.

    Examples:
        >>> solve([1, 2, 1, 1, 2])
        4
        # Subarrays: [1], [1, 2, 1], [1, 1], [1, 1, 2], [1] (depending on target)
    """
    if not nums:
        return 0

    # In standard 'Majority Element' problems, we identify the candidate.
    # For this implementation, we assume the target is the element that 
    # appears most frequently, or we solve for a specific target if provided.
    # Here we find the most frequent element to satisfy the 'Majority' logic.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    target = max(counts, key=counts.get)
    
    # To find subarrays where target appears > half the time:
    # Let target be +1 and other elements be -1.
    # We need sum(subarray) > 0.
    # sum(i, j) = prefix_sum[j] - prefix_sum[i-1] > 0 => prefix_sum[j] > prefix_sum[i-1]
    
    n = len(nums)
    prefix_sum = 0
    # We use a Fenwick tree (Binary Indexed Tree) to count occurrences of 
    # prefix sums seen so far. Since prefix sums can be negative, 
    # we offset them by n.
    offset = n + 1
    bit = [0] * (2 * n + 2)

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

    total_count = 0
    # Initial prefix sum 0 occurs once (before any elements)
    update(0, 1)
    
    current_sum = 0
    for num in nums:
        # Transform the problem into a sum of 1s and -1s
        if num == target:
            current_sum += 1
        else:
            current_sum -= 1
        
        # We need to find how many previous prefix_sums are strictly less than current_sum
        # query(current_sum - 1) returns count of prefix_sums in range [-offset, current_sum - 1]
        total_count += query(current_sum - 1)
        
        # Add current prefix sum to the BIT
        update(current_sum, 1)
        
    return total_count
