METADATA = {
    "id": 18,
    "name": "4Sum",
    "slug": "4sum",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1) or O(n) depending on sorting implementation",
    "description": "Find all unique quadruplets in an array that sum up to a specific target.",
}

def solve(nums: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique quadruplets in the array that sum up to the target.

    Args:
        nums: A list of integers.
        target: The integer target sum.

    Returns:
        A list of lists, where each inner list contains four unique integers 
        from the input array that sum to the target.

    Examples:
        >>> solve([1, 0, -1, 0, -2, 2], 0)
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> solve([2, 2, 2, 2, 2], 8)
        [[2, 2, 2, 2]]
    """
    nums.sort()
    n = len(nums)
    results = []

    for i in range(n - 3):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Optimization: Smallest possible sum with nums[i] is too large
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # Optimization: Largest possible sum with nums[i] is too small
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate values for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            # Optimization: Smallest possible sum with nums[i], nums[j] is too large
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            # Optimization: Largest possible sum with nums[i], nums[j] is too small
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            # Two-pointer approach for the remaining two numbers
            left = j + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if current_sum == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
    return results
