METADATA = {
    "id": 274,
    "name": "H-Index",
    "slug": "h-index",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "counting_sort", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of h such that the researcher has published at least h papers that have each been cited at least h times.",
}

def solve(citations: list[int]) -> int:
    """
    Calculates the H-Index of a researcher using a bucket sort approach.

    The H-Index is defined as the maximum value h such that the researcher 
    has published at least h papers that have each been cited at least h times.

    Args:
        citations: A list of integers representing the number of citations for each paper.

    Returns:
        The H-Index of the researcher.

    Examples:
        >>> solve([3, 0, 6, 1, 5])
        3
        >>> solve([1, 3, 1])
        1
        >>> solve([0])
        0
    """
    n = len(citations)
    # Create buckets to store counts of citations. 
    # Any citation count greater than n is treated as n because 
    # the H-index cannot exceed the total number of papers.
    buckets = [0] * (n + 1)

    for citation in citations:
        if citation >= n:
            buckets[n] += 1
        else:
            buckets[citation] += 1

    # Iterate backwards through the buckets to accumulate the count of papers.
    # We want to find the largest h such that the sum of papers with 
    # citations >= h is at least h.
    total_papers_with_at_least_h_citations = 0
    for h in range(n, -1, -1):
        total_papers_with_at_least_h_citations += buckets[h]
        if total_papers_with_at_least_h_citations >= h:
            return h

    return 0
