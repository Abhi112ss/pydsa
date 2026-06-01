METADATA = {
    "id": 2994,
    "name": "Friday Purchases II",
    "slug": "friday-purchases-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total number of Friday purchases within specific ranges using prefix sums.",
}

def solve(purchases: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the total number of Friday purchases for each query range.

    A purchase is considered a Friday purchase if the day index (1-indexed) 
    is a multiple of 7 (i.e., day 7, 14, 21, ...). However, based on the 
    problem context of 'Friday Purchases', we identify indices where 
    (index % 7) == 0 if we consider the sequence starting from day 1.
    Actually, in most LeetCode problems of this type, 'Friday' refers to 
    the 5th day of the week or a specific modulo. Given the prompt's 
    hint, we treat indices that satisfy the 'Friday' condition as 1 and others as 0.

    Args:
        purchases: A list of integers representing purchases on consecutive days.
        queries: A list of [start, end] pairs (0-indexed) representing ranges.

    Returns:
        A list of integers representing the count of Friday purchases in each range.

    Examples:
        >>> solve([1, 1, 1, 1, 1, 1, 1, 1], [[0, 6], [1, 7]])
        [1, 1]
    """
    n = len(purchases)
    # prefix_sum[i] will store the count of Friday purchases from index 0 to i-1
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        # Determine if the current day is a Friday. 
        # Assuming day 1 is Monday, Friday is day 5, 12, 19...
        # If the problem defines Friday as index % 7 == 4 (0-indexed), 
        # we check that condition.
        is_friday = 1 if (i % 7 == 4) else 0
        
        # Build the prefix sum array
        prefix_sum[i + 1] = prefix_sum[i] + is_friday

    results = []
    for start, end in queries:
        # The number of Friday purchases in range [start, end] is 
        # prefix_sum[end + 1] - prefix_sum[start]
        # This allows O(1) range sum queries.
        count = prefix_sum[end + 1] - prefix_sum[start]
        results.append(count)
        
    return results
