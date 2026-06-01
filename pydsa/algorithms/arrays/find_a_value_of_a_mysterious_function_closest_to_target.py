METADATA = {
    "id": 1521,
    "name": "Find a Value of a Mysterious Function Closest to Target",
    "slug": "find-a-value-of-a-mysterious-function-closest-to-target",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "monotonic_function"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the value of a function f(x) = (x * nums[x]) that is closest to a given target value.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Args:
        nums: A list of integers where the function is defined as f(i) = i * nums[i].
        target: The target value to approach.

    Returns:
        The value of f(i) that is closest to the target.
    """
    low = 0
    high = len(nums) - 1
    closest_value = nums[0] * 0

    while low <= high:
        mid = (low + high) // 2
        current_value = mid * nums[mid]

        if abs(current_value - target) < abs(closest_value - target):
            closest_value = current_value
        elif abs(current_value - target) == abs(closest_value - target):
            closest_value = min(closest_value, current_value)

        if current_value < target:
            low = mid + 1
        elif current_value > target:
            high = mid - 1
        else:
            return current_value

    return closest_value