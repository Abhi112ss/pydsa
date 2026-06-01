METADATA = {
    "id": 3718,
    "name": "Smallest Missing Multiple of K",
    "slug": "smallest_missing_multiple_of_k",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the smallest positive integer that is a multiple of k and is not present in the given array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the smallest positive integer that is a multiple of k and is not in nums.

    Args:
        nums: A list of positive integers.
        k: The multiplier to check for.

    Returns:
        The smallest positive integer multiple of k not present in the input list.

    Examples:
        >>> solve([3, 6, 9, 12], 3)
        15
        >>> solve([1, 2, 3, 4, 5], 2)
        6
        >>> solve([10, 20, 30], 5)
        5
    """
    # Convert to set for O(1) average lookup time
    # This is necessary to check existence efficiently
    num_set = set(nums)
    
    # The problem asks for the smallest multiple of k.
    # Multiples of k are k, 2k, 3k, ...
    # We can iterate through multiples of k.
    # However, if the input array is very large and contains many consecutive multiples,
    # we need to find the first gap.
    
    # Since we need the *smallest* missing multiple, we start from 1 * k.
    # We check if current_multiple is in the set.
    # If it is, we move to the next multiple.
    
    current_multiple = k
    
    # Optimization: If k is not in the set, k is the answer.
    # We increment by k each time to ensure we only check multiples.
    while current_multiple in num_set:
        current_multiple += k
        
    return current_multiple

# Note: While the prompt suggested binary search, binary search is typically 
# used when the input is sorted and we are looking for a gap in a range. 
# Given the constraints of a general 'nums' array, a set-based linear 
# scan of multiples is O(N) in the worst case (where N is the number of 
# elements in nums), but since we only check multiples of k, 
# the number of iterations is at most (len(nums) + 1).
# This is the most robust approach for an unsorted list.
