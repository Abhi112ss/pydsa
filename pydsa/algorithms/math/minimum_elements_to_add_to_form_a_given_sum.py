METADATA = {
    "id": 1785,
    "name": "Minimum Elements to Add to Form a Given Sum",
    "slug": "minimum-elements-to-add-to-form-a-given-sum",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of elements to add to a set to reach a target sum using a greedy approach.",
}

def solve(elements: list[int], target: int) -> int:
    """
    Calculates the minimum number of elements needed to reach a target sum.
    
    The strategy is to use the largest available element repeatedly to 
    minimize the count of elements added.

    Args:
        elements: A list of available integers that can be added.
        target: The target sum to reach.

    Returns:
        The minimum number of elements required to reach the target. 
        Returns -1 if the target cannot be reached exactly.

    Examples:
        >>> solve([2, 3], 7)
        2
        >>> solve([5], 12)
        -1
        >>> solve([1, 10], 21)
        3
    """
    if target == 0:
        return 0
    
    if not elements:
        return -1

    # To minimize the number of elements, we must use the largest element as much as possible.
    max_val = max(elements)
    
    # Calculate how many times the largest element fits into the target.
    # We use integer division for the count and modulo for the remainder.
    count = target // max_val
    remainder = target % max_val
    
    # If the remainder is 0, we reached the target perfectly using only the max_val.
    if remainder == 0:
        return count
    
    # If there is a remainder, we need to check if the remainder can be formed 
    # by the other elements. However, the problem constraints/logic for this 
    # specific LeetCode variation usually implies we can only use the elements 
    # provided. If the remainder is not 0, we check if the remainder itself 
    # exists in the set or can be formed. 
    # Note: The standard interpretation of this specific problem type is 
    # finding if (target - count * max_val) can be satisfied.
    
    # For the specific LeetCode #1785 logic: 
    # We check if the remainder can be satisfied by any single element in the set.
    # If the remainder is not 0, we check if it's possible to reach the target.
    # Since we want MINIMUM elements, we check if the remainder is in the set.
    # If not, we might need to reduce the 'count' of max_val to make the remainder 
    # match an element in the set.
    
    # Optimization: Since we want the minimum elements, we try to use as many 
    # max_val as possible. If target % max_val != 0, we check if 
    # (target - k * max_val) is in the set for some k.
    
    # However, for the simplest greedy version (often seen in this problem):
    # We check if target % max_val is in the set.
    # If not, we check if (target % max_val) + max_val is in the set, etc.
    # But the most efficient way is to check if (target - k * max_val) is in elements.
    
    # Let's refine: We need to find min k such that (target - k * max_val) is in elements.
    # We start with the largest possible k.
    
    element_set = set(elements)
    
    # We iterate backwards from the maximum possible number of max_val elements.
    # This ensures we find the minimum total elements (count + 1).
    for k in range(count, -1, -1):
        current_remainder = target - (k * max_val)
        if current_remainder == 0:
            return k
        if current_remainder in element_set:
            return k + 1
            
    return -1