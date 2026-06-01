METADATA = {
    "id": 3682,
    "name": "Minimum Index Sum of Common Elements",
    "slug": "minimum_index_sum_of_common_elements",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(min(n, m))",
    "description": "Find the minimum sum of indices for common elements between two arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Finds the minimum sum of indices for common elements between two arrays.
    
    The problem asks for the minimum sum of indices (1-indexed) for any element 
    that appears in both arrays. Since we want the minimum sum, we look for 
    the first occurrence of each common element in both arrays.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.

    Returns:
        The minimum sum of 1-based indices of a common element, or -1 if no common element exists.

    Examples:
        >>> solve([1, 2, 3], [2, 4, 1])
        3  # Element 1 is at index 1 in nums1 and index 3 in nums2 (sum 4). 
           # Element 2 is at index 2 in nums1 and index 1 in nums2 (sum 3). Min is 3.
        >>> solve([1, 2, 3], [4, 5, 6])
        -1
    """
    # Map to store the first occurrence (1-indexed) of each number in nums1
    # We only care about the first occurrence because it yields the minimum index sum
    first_occurrence_map: dict[int, int] = {}
    
    for index, value in enumerate(nums1):
        if value not in first_occurrence_map:
            first_occurrence_map[value] = index + 1
            
    min_index_sum = float('inf')
    found_common = False
    
    # Iterate through nums2 to find elements present in nums1
    for index, value in enumerate(nums2):
        if value in first_occurrence_map:
            found_common = True
            # Calculate the sum of 1-based indices
            current_sum = first_occurrence_map[value] + (index + 1)
            # Update the global minimum sum
            if current_sum < min_index_sum:
                min_index_sum = current_sum
                
    # If no common element was found, return -1 as per problem requirements
    if not found_common:
        return -1
        
    return int(min_index_sum)
