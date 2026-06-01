METADATA = {
    "id": 3564,
    "name": "Seasonal Sales Analysis",
    "slug": "seasonal_sales_analysis",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total sales within specific seasonal ranges using prefix sums.",
}

def solve(sales: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the total sales for multiple seasonal ranges using prefix sums.

    Args:
        sales: A list of integers representing daily sales.
        queries: A list of lists, where each sub-list contains [start_index, end_index].

    Returns:
        A list of integers representing the sum of sales for each query range.

    Examples:
        >>> solve([10, 20, 30, 40, 50], [[0, 2], [1, 3], [2, 4]])
        [60, 90, 120]
        >>> solve([1, 1, 1, 1], [[0, 3]])
        [4]
    """
    n = len(sales)
    if n == 0:
        return [0] * len(queries)

    # Precompute prefix sums to allow O(1) range sum queries.
    # prefix_sums[i] stores the sum of sales from index 0 to i-1.
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + sales[i]

    results = []
    for start, end in queries:
        # Ensure indices are within valid bounds to prevent errors.
        # The sum for range [start, end] is prefix_sums[end + 1] - prefix_sums[start].
        # We use end + 1 because prefix_sums is 1-indexed relative to the sales array.
        actual_start = max(0, start)
        actual_end = min(n - 1, end)

        if actual_start > actual_end:
            results.append(0)
        else:
            range_sum = prefix_sums[actual_end + 1] - prefix_sums[actual_start]
            results.append(range_sum)

    return results
