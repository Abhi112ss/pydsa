METADATA = {
    "id": 3424,
    "name": "Minimum Cost to Make Arrays Identical",
    "slug": "minimum-cost-to-make-arrays-identical",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to make two arrays identical by rearranging elements, which is the sum of absolute differences of sorted arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum cost to make two arrays identical.
    
    The minimum cost is achieved by sorting both arrays and summing the 
    absolute differences between elements at the same index. This is a 
    greedy approach based on the rearrangement inequality.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The minimum total cost as an integer.

    Examples:
        >>> solve([1, 3, 5], [2, 4, 6])
        3
        >>> solve([1, 1, 1], [1, 1, 1])
        0
    """
    # Sort both arrays to pair the smallest elements together, 
    # the second smallest together, and so on.
    nums1.sort()
    nums2.sort()
    
    total_cost = 0
    
    # Iterate through the sorted arrays and accumulate the absolute 
    # difference between corresponding elements.
    for val1, val2 in zip(nums1, nums2):
        total_cost += abs(val1 - val2)
        
    return total_cost
