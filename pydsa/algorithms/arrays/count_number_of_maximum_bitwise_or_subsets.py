METADATA = {
    "id": 2044,
    "name": "Count Number of Maximum Bitwise-OR Subsets",
    "slug": "count-number-of-maximum-bitwise-or-subsets",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "subset"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Count the number of non-empty subsets of an array that have the maximum possible bitwise OR value.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of subsets that result in the maximum bitwise OR value.

    Args:
        nums: A list of integers.

    Returns:
        The count of subsets whose bitwise OR equals the maximum possible OR.

    Examples:
        >>> solve([3, 2, 1, 5])
        6
        >>> solve([1, 1, 2])
        3
    """
    # The maximum possible bitwise OR is the OR of all elements in the array
    max_or = 0
    for num in nums:
        max_or |= num

    n = len(nums)
    count = 0

    def backtrack(index: int, current_or: int) -> None:
        nonlocal count
        
        # Base case: if we have considered all elements
        if index == n:
            if current_or == max_or:
                count += 1
            return

        # Option 1: Include nums[index] in the subset
        backtrack(index + 1, current_or | nums[index])

        # Option 2: Exclude nums[index] from the subset
        backtrack(index + 1, current_or)

    # Start recursion from the first index with an initial OR of 0
    backtrack(0, 0)
    return count
