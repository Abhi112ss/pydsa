METADATA = {
    "id": 15,
    "name": "3Sum",
    "slug": "3sum",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1) or O(n) depending on sorting implementation",
    "description": "Find all unique triplets in an array that sum up to zero.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the array which gives the sum of zero.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list is a unique triplet that sums to zero.

    Examples:
        >>> solve([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> solve([0, 1, 1])
        []
        >>> solve([0, 0, 0])
        [[0, 0, 0]]
    """
    results: list[list[int]] = []
    n = len(nums)
    
    # Sorting allows us to use the two-pointer approach and easily skip duplicates
    nums.sort()

    for i in range(n - 2):
        # If the current smallest number is greater than 0, no triplet can sum to 0
        if nums[i] > 0:
            break

        # Skip the same element to avoid duplicate triplets in the result
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left_pointer = i + 1
        right_pointer = n - 1

        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

            if current_sum < 0:
                # Sum is too small, move the left pointer to increase the sum
                left_pointer += 1
            elif current_sum > 0:
                # Sum is too large, move the right pointer to decrease the sum
                right_pointer -= 1
            else:
                # Found a valid triplet
                results.append([nums[i], nums[left_pointer], nums[right_pointer]])

                # Skip duplicate values for the left pointer
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                    left_pointer += 1
                # Skip duplicate values for the right pointer
                while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                    right_pointer -= 1

                # Move both pointers inward after finding a valid triplet
                left_pointer += 1
                right_pointer -= 1

    return results
