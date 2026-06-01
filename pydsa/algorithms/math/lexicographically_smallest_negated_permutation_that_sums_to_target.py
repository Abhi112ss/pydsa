METADATA = {
    "id": 3752,
    "name": "Lexicographically Smallest Negated Permutation that Sums to Target",
    "slug": "lexicographically-smallest-negated-permutation-that-sums-to-target",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest permutation of a given set of integers (allowing negation) that sums to a specific target.",
}

def solve(nums: list[int], target: int) -> list[int]:
    """
    Args:
        nums: A list of integers to be used in the permutation.
        target: The required sum of the permutation.

    Returns:
        The lexicographically smallest permutation of negated or original values that sums to target, 
        or an empty list if no such permutation exists.
    """
    n = len(nums)
    sorted_nums = sorted(nums)
    
    possible_values = []
    for x in sorted_nums:
        possible_values.append(-abs(x))
        possible_values.append(abs(x))
    
    possible_values.sort()
    
    current_permutation = []
    current_sum = 0
    used_indices = set()
    
    available_elements = []
    for i in range(n):
        available_elements.append((-abs(sorted_nums[i]), i))
        available_elements.append((abs(sorted_nums[i]), i))
    
    available_elements.sort()

    def get_min_sum(remaining_indices: set[int], current_sum: int) -> int:
        min_s = current_sum
        for idx in remaining_indices:
            min_s -= abs(sorted_nums[idx])
        return min_s

    def get_max_sum(remaining_indices: set[int], current_sum: int) -> int:
        max_s = current_sum
        for idx in remaining_indices:
            max_s += abs(sorted_nums[idx])
        return max_s

    remaining_indices = set(range(n))
    result = []
    running_sum = 0

    for i in range(n):
        found = False
        
        options = []
        for idx in remaining_indices:
            options.append((-abs(sorted_nums[idx]), idx))
            options.append((abs(sorted_nums[idx]), idx))
        
        options.sort()

        for val, idx in options:
            new_sum = running_sum + val
            temp_remaining = remaining_indices.copy()
            temp_remaining.remove(idx)
            
            min_possible = new_sum
            max_possible = new_sum
            for r_idx in temp_remaining:
                min_possible -= abs(sorted_nums[r_idx])
                max_possible += abs(sorted_nums[r_idx])
            
            if min_possible <= target <= max_possible:
                result.append(val)
                running_sum = new_sum
                remaining_indices.remove(idx)
                found = True
                break
        
        if not found:
            return []

    if running_sum != target:
        return []
        
    return result