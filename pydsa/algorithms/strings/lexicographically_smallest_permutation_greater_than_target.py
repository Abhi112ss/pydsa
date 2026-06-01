METADATA = {
    "id": 3720,
    "name": "Lexicographically Smallest Permutation Greater Than Target",
    "slug": "lexicographically-smallest-permutation-greater-than-target",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest permutation of a given set of digits that is strictly greater than a target number.",
}

def solve(digits: list[int], target: list[int]) -> list[int] | None:
    """
    Finds the lexicographically smallest permutation of digits that is 
    strictly greater than the target list.

    Args:
        digits: A list of integers representing the available digits.
        target: A list of integers representing the target number.

    Returns:
        A list of integers representing the smallest permutation greater than target,
        or None if no such permutation exists.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3])
        [1, 3, 2]
        >>> solve([1, 2, 3], [3, 2, 1])
        None
    """
    n = len(target)
    if len(digits) < n:
        return None
    
    # If we have more digits than the target length, the smallest permutation
    # is simply the sorted digits (this handles cases where target is shorter).
    # However, the problem implies same length or specific constraints.
    # Assuming same length based on standard permutation problems.
    if len(digits) > n:
        sorted_digits = sorted(digits)
        return sorted_digits[:n]

    # Count frequencies of available digits
    counts = [0] * 10
    for d in digits:
        counts[d] += 1

    # We try to match the target prefix as long as possible.
    # We need to find the rightmost index 'i' where we can place a digit 
    # strictly greater than target[i], while the prefix [0...i-1] matches target.
    
    # first, check if we can match the target exactly (not allowed, must be greater)
    # so we look for the pivot point.
    
    best_pivot = -1
    best_digit = -1
    
    # current_counts tracks digits used to match the prefix
    current_counts = [0] * 10
    
    # Step 1: Try to match the prefix
    for i in range(n):
        # Check if we can place a digit > target[i] at this position
        # to create a valid permutation greater than target.
        for d in range(target[i] + 1, 10):
            if counts[d] - current_counts[d] > 0:
                best_pivot = i
                best_digit = d
                break
        
        # Try to continue matching the target prefix
        target_digit = target[i]
        if counts[target_digit] - current_counts[target_digit] > 0:
            current_counts[target_digit] += 1
        else:
            # Cannot match prefix further
            break
    else:
        # If we completed the loop, it means we matched the target exactly.
        # But we need strictly greater, so the pivot logic above handles it.
        pass

    if best_pivot == -1:
        return None

    # Step 2: Construct the result
    # Re-calculate counts for the prefix up to best_pivot
    result = [0] * n
    final_counts = [0] * 10
    for d in digits:
        final_counts[d] += 1
        
    # Fill prefix matching target
    for i in range(best_pivot):
        result[i] = target[i]
        final_counts[target[i]] -= 1
        
    # Fill the pivot
    result[best_pivot] = best_digit
    final_counts[best_digit] -= 1
    
    # Fill the rest with the smallest available digits (sorted)
    remaining_digits = []
    for d in range(10):
        remaining_digits.extend([d] * final_counts[d])
    
    # remaining_digits is already sorted because we iterated d from 0 to 9
    for i in range(best_pivot + 1, n):
        result[i] = remaining_digits[i - (best_pivot + 1)]
        
    return result
