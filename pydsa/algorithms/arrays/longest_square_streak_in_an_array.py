METADATA = {
    "id": 2501,
    "name": "Longest Square Streak in an Array",
    "slug": "longest-square-streak-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest streak of numbers where each subsequent number is the square of the previous one.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest square streak in the given array.

    A square streak is a sequence of numbers where each number is the square 
    of the previous number in the sequence.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest square streak found. Returns 0 if no streak 
        of length at least 2 is found (though the problem implies returning 
        the max length, usually 1 if no squares exist, but LeetCode 
        specifies returning the max length found).

    Examples:
        >>> solve([2, 3, 5, 6, 7])
        1
        >>> solve([4, 3, 6, 16, 8, 2])
        3
        >>> solve([2, 4, 16, 256, 65536])
        5
    """
    # Use a set for O(1) average time complexity lookups
    unique_nums = set(nums)
    # Sort the unique numbers to process them in increasing order
    sorted_nums = sorted(list(unique_nums))
    
    max_streak = 1
    # Keep track of visited numbers to avoid redundant calculations
    visited = set()

    for num in sorted_nums:
        if num in visited:
            continue
            
        current_streak = 0
        current_val = num
        
        # Iteratively find the next square in the sequence
        while current_val in unique_nums:
            visited.add(current_val)
            current_streak += 1
            # Calculate the next square
            current_val = current_val * current_val
            
            # Safety break for extremely large numbers that might exceed 
            # practical integer limits or cause overflow in other languages,
            # though Python handles arbitrary precision.
            if current_val > 10**5: # Based on LeetCode constraints (nums[i] <= 10^5)
                # We still check if it's in unique_nums, but if current_val 
                # is already > 10^5, it can't be in the set.
                if current_val in unique_nums:
                    current_streak += 1
                    visited.add(current_val)
                break

        max_streak = max(max_streak, current_streak)

    # The problem asks for the longest streak. If the longest streak is 1, 
    # it means no number was the square of another.
    return max_streak if max_streak >= 2 else 1
