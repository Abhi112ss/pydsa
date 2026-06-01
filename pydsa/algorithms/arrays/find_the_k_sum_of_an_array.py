METADATA = {
    "id": 2386,
    "name": "Find the K-Sum of an Array",
    "slug": "find-the-k-sum-of-an-array",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n^(k-1))",
    "space_complexity": "O(k)",
    "description": "Find all unique combinations of k numbers from an array that sum up to a given target.",
}

def solve(nums: list[int], k: int, target: int) -> list[list[int]]:
    """
    Args:
        nums: A list of integers.
        k: The number of elements to sum.
        target: The target sum.

    Returns:
        A list of lists, where each inner list is a unique combination of k elements that sum to target.
    """
    nums.sort()
    results = []

    def k_sum_recursive(start_index: int, current_k: int, current_target: int, path: list[int]) -> None:
        if current_k == 2:
            left = start_index
            right = len(nums) - 1
            while left < right:
                sum_two = nums[left] + nums[right]
                if sum_two == current_target:
                    results.append(path + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum_two < current_target:
                    left += 1
                else:
                    right -= 1
            return

        for i in range(start_index, len(nums) - current_k + 1):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] * current_k > current_target:
                break
            
            if nums[i] + (nums[-1] * (current_k - 1)) < current_target:
                continue

            k_sum_recursive(i + 1, current_k - 1, current_target - nums[i], path + [nums[i]])

    k_sum_recursive(0, k, target, [])
    return results