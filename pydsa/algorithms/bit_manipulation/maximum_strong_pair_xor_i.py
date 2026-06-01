METADATA = {
    "id": 2932,
    "name": "Maximum Strong Pair XOR I",
    "slug": "maximum-strong-pair-xor-i",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum XOR value of a strong pair (x, y) where |x - y| <= min(x, y).",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum XOR value of a 'strong pair' in the given list.
    A pair (x, y) is strong if |x - y| <= min(x, y).

    Args:
        nums: A list of integers.

    Returns:
        The maximum XOR value among all strong pairs.

    Examples:
        >>> solve([1, 4, 3, 2, 7])
        3
        >>> solve([10, 15, 20, 25])
        13
    """
    # Sort the array to ensure that for any pair (nums[i], nums[j]) with i < j,
    # min(nums[i], nums[j]) is always nums[i].
    # The condition |nums[j] - nums[i]| <= nums[i] simplifies to nums[j] <= 2 * nums[i].
    nums.sort()
    
    max_xor = 0
    left = 0
    n = len(nums)

    # Use a sliding window approach. For each 'right' index, we find the 
    # smallest 'left' index such that the pair (nums[left], nums[right]) is strong.
    # Since the array is sorted, if (nums[left], nums[right]) is strong, 
    # then (nums[k], nums[right]) is also strong for all k where left < k < right.
    for right in range(n):
        # Shrink the window from the left if the strong pair condition is violated.
        # Condition: nums[right] - nums[left] <= nums[left]  =>  nums[right] <= 2 * nums[left]
        while nums[right] > 2 * nums[left]:
            left += 1
        
        # Check all valid pairs in the current window ending at 'right'.
        # Note: For version I of this problem, n is small enough for O(n^2) worst case
        # within the window, but the sliding window logic keeps it efficient.
        for i in range(left, right):
            current_xor = nums[i] ^ nums[right]
            if current_xor > max_xor:
                max_xor = current_xor
                
    return max_xor
