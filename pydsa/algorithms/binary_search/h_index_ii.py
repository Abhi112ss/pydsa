METADATA = {
    "id": 275,
    "name": "H-Index II",
    "slug": "h-index-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Given a sorted array of citations, find the h-index using binary search.",
}

def solve(citations: list[int]) -> int:
    """
    Finds the h-index for a given sorted list of citations.

    The h-index is defined as the maximum value of h such that the given 
    author/journal has published at least h papers that have each been 
    cited at least h times.

    Args:
        citations: A list of integers representing citations, sorted in non-decreasing order.

    Returns:
        The h-index as an integer.

    Examples:
        >>> solve([0, 1, 3, 5, 6])
        3
        >>> solve([1, 2, 3])
        2
        >>> solve([10, 10, 10])
        3
        >>> solve([0])
        0
    """
    n = len(citations)
    left = 0
    right = n - 1
    h_index = 0

    while left <= right:
        mid = left + (right - left) // 2
        
        # The number of papers with at least citations[mid] citations 
        # is the count of elements from index 'mid' to the end of the array.
        papers_count = n - mid

        if citations[mid] >= papers_count:
            # If the current citation count is enough to satisfy the h-index 
            # requirement for 'papers_count' papers, this is a potential h-index.
            # We try to find a larger h-index by moving left (increasing papers_count).
            h_index = papers_count
            right = mid - 1
        else:
            # If citations[mid] is too small, we need more citations per paper,
            # so we move to the right to increase the citation value.
            left = mid + 1

    return h_index
