METADATA = {
    "id": 321,
    "name": "Create Maximum Number",
    "slug": "create-maximum-number",
    "category": "Hard",
    "aliases": [],
    "tags": ["monotonic_stack", "greedy", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(k * (m + n)^2)",
    "space_complexity": "O(m + n)",
    "description": "Find the maximum number of length k that can be formed by selecting digits from two arrays while maintaining relative order.",
}

def solve(digits1: list[int], digits2: list[int], k: int) -> list[int]:
    """
    Finds the maximum number of length k that can be formed by selecting digits 
    from two arrays while maintaining their relative order.

    Args:
        digits1: The first array of digits.
        digits2: The second array of digits.
        k: The target length of the resulting number.

    Returns:
        A list of integers representing the maximum number.

    Examples:
        >>> solve([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
        [9, 6, 5, 8, 3]
        >>> solve([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 1)
        [9]
    """
    m, n = len(digits1), len(digits2)

    def get_max_subsequence(nums: list[int], length: int) -> list[int]:
        """Uses a monotonic stack to find the largest subsequence of a given length."""
        stack = []
        to_drop = len(nums) - length
        for digit in nums:
            # While we have digits to drop and the current digit is larger than the stack top
            while to_drop > 0 and stack and stack[-1] < digit:
                stack.pop()
                to_drop -= 1
            stack.append(digit)
        # If we haven't dropped enough, slice the end
        return stack[:length]

    def merge_max(arr1: list[int], arr2: list[int]) -> list[int]:
        """Merges two arrays to create the largest possible number greedily."""
        merged = []
        i, j = 0, 0
        while i < len(arr1) or j < len(arr2):
            # Compare suffixes to decide which element to pick next
            if arr1[i:] > arr2[j:]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        return merged

    max_result = []

    # Iterate through all possible lengths i for digits1 and k-i for digits2
    # Constraints: 0 <= i <= m and 0 <= k-i <= n
    # This implies: max(0, k - n) <= i <= min(k, m)
    start_i = max(0, k - n)
    end_i = min(k, m)

    for i in range(start_i, end_i + 1):
        # 1. Get the best subsequence of length i from digits1
        # 2. Get the best subsequence of length k-i from digits2
        # 3. Merge them to get the best possible number for this specific split
        sub1 = get_max_subsequence(digits1, i)
        sub2 = get_max_subsequence(digits2, k - i)
        combined = merge_max(sub1, sub2)
        
        # Update the global maximum
        if combined > max_result:
            max_result = combined

    return max_result
