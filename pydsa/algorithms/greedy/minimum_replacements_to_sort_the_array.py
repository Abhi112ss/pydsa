METADATA = {
    "id": 2366,
    "name": "Minimum Replacements to Sort the Array",
    "slug": "minimum-replacements-to-sort-the-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of replacements to make an array non-decreasing by replacing an element with any value between 1 and itself.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of replacements needed to make the array non-decreasing.

    The strategy is to iterate from right to left. For each element, if it is greater 
    than the element to its right, we must reduce it. To minimize future replacements, 
    we should reduce it to the largest possible value that is still less than or 
    equal to the element to its right. If we need to split an element into multiple 
    parts to satisfy the non-decreasing property, we distribute the value as evenly 
    as possible to keep the new 'minimum' value as large as possible.

    Args:
        nums: A list of positive integers.

    Returns:
        The minimum number of replacements required.

    Examples:
        >>> solve([3, 9, 3])
        3
        >>> solve([1, 1, 1])
        0
        >>> solve([5, 2, 6])
        1
    """
    total_replacements = 0
    n = len(nums)
    
    # We start from the second to last element and move backwards.
    # The last element is our initial 'upper_bound' for the element to its left.
    upper_bound = nums[-1]
    
    for i in range(n - 2, -1, -1):
        current_val = nums[i]
        
        if current_val > upper_bound:
            # We need to split current_val into 'k' pieces such that 
            # each piece is <= upper_bound.
            # The minimum number of pieces k is ceil(current_val / upper_bound).
            # Using integer math: (current_val + upper_bound - 1) // upper_bound
            num_pieces = (current_val + upper_bound - 1) // upper_bound
            
            # The number of replacements for this element is (number of pieces - 1).
            total_replacements += (num_pieces - 1)
            
            # To keep the next element (to the left) as large as possible,
            # we want the smallest piece in this split to be as large as possible.
            # The largest possible value for the smallest piece is floor(current_val / num_pieces).
            upper_bound = current_val // num_pieces
        else:
            # If current_val is already <= upper_bound, no replacement is needed.
            # The new upper_bound for the next element is simply current_val.
            upper_bound = current_val
            
    return total_replacements
