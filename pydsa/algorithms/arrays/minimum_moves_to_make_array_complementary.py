METADATA = {
    "id": 1674,
    "name": "Minimum Moves to Make Array Complementary",
    "slug": "minimum-moves-to-make-array-complementary",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array complementary to a target value using a difference array approach.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Args:
        nums: A list of integers.
        target: The target value for the array to be complementary to.

    Returns:
        The minimum number of operations required.
    """
    n = len(nums)
    diff = [0] * (n + 1)
    current_operations = 0

    for x in nums:
        complement = target - x
        if complement < 0:
            current_operations += 1
        elif complement < n:
            diff[complement] += 1
            diff[complement + 1] -= 1

    min_operations = current_operations
    for i in range(n):
        current_operations += diff[i]
        if current_operations < min_operations:
            min_operations = current_operations

    return min_operations