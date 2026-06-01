METADATA = {
    "id": 180,
    "name": "Consecutive Numbers",
    "slug": "consecutive_numbers",
    "category": "Algorithms",
    "aliases": ["Consecutive Numbers Python"],
    "tags": ["logic", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find all numbers that appear at least three times consecutively in a sequence.",
}


def solve(nums: list[int]) -> list[int]:
    """Finds all numbers that appear at least three times consecutively.

    Args:
        nums: A list of integers representing the sequence.

    Returns:
        A list of unique integers that appear consecutively at least three times.

    Examples:
        >>> solve([1, 1, 1, 2, 1, 2, 2, 2])
        [1, 2]
        >>> solve([1, 2, 3, 4])
        []
    """
    # Use a set to store unique numbers that meet the criteria
    consecutive_matches = set()
    
    # Iterate through the list up to the third-to-last element
    # to avoid index out of bounds errors when checking i+1 and i+2
    for index in range(len(nums) - 2):
        # Check if the current element is identical to the next two elements
        if nums[index] == nums[index + 1] == nums[index + 2]:
            consecutive_matches.add(nums[index])
            
    # Return the results as a list as per standard LeetCode output requirements
    return list(consecutive_matches)
