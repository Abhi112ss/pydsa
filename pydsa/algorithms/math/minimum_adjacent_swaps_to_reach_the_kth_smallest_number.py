METADATA = {
    "id": 1850,
    "name": "Minimum Adjacent Swaps to Reach the Kth Smallest Number",
    "slug": "minimum-adjacent-swaps-to-reach-the-kth-smallest-number",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of adjacent swaps required to transform an array into its Kth smallest permutation.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers representing the initial array.
        k: The target permutation index (1-indexed).

    Returns:
        The minimum number of adjacent swaps required to reach the Kth smallest permutation.
    """
    n = len(nums)
    sorted_nums = sorted(nums)
    target_permutation = []
    
    k_minus_one = k - 1
    available_elements = sorted_nums[:]
    
    import math
    
    for i in range(n, 0, -1):
        factorial = math.factorial(i - 1)
        index = k_minus_one // factorial
        target_permutation.append(available_elements.pop(index))
        k_minus_one %= factorial
        
    swaps = 0
    current_array = nums[:]
    
    for i in range(n):
        target_val = target_permutation[i]
        
        current_index = -1
        for j in range(i, n):
            if current_array[j] == target_val:
                current_index = j
                break
        
        swaps += (current_index - i)
        
        element_to_move = current_array.pop(current_index)
        current_array.insert(i, element_to_move)
        
    return swaps