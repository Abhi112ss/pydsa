METADATA = {
    "id": 3040,
    "name": "Maximum Number of Operations With the Same Score II",
    "slug": "maximum-number-of-operations-with-the-same-score-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "binary_search", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of operations to remove elements such that the sum of removed elements is equal, given a starting index constraint.",
}

def solve(nums: list[int], index: int) -> int:
    """
    Args:
        nums: A list of integers representing the scores.
        index: The index from which operations must start.

    Returns:
        The maximum number of operations possible.
    """
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    def count_operations(start_idx: int, end_idx: int) -> int:
        left = start_idx
        right = end_idx
        max_ops = 0
        
        while left < right:
            sum_left = nums[left]
            sum_right = nums[right]
            
            if sum_left == sum_right:
                max_ops += 1
                left += 1
                right -= 1
            elif sum_left < sum_right:
                left += 1
            else:
                right -= 1
        return max_ops

    def get_max_ops_with_target_sum(left_range: range, right_range: range) -> int:
        left_ptr = left_range.start
        right_ptr = right_range.start
        
        total_left_sum = 0
        total_right_sum = 0
        
        count = 0
        
        l_idx = left_range.start
        r_idx = right_range.start
        
        current_left_sum = 0
        current_right_sum = 0
        
        res = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        ops = 0
        
        l_idx = left_range.start
        r_idx = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0
        
        l_ptr = left_range.start
        r_ptr = right_range.start
        
        l_sum = 0
        r_sum = 0