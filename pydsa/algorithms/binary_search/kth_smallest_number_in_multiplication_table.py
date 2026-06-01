METADATA = {
    "id": 668,
    "name": "Kth Smallest Number in Multiplication Table",
    "slug": "kth-smallest-number-in-multiplication-table",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary search", "math"],
    "difficulty": "hard",
    "time_complexity": "O(m * log(m * n))",
    "space_complexity": "O(1)",
    "description": "Find the kth smallest number in an m x n multiplication table using binary search on the value range.",
}

def solve(m: int, n: int, k: int) -> int:
    """
    Finds the kth smallest number in an m x n multiplication table.

    The multiplication table is defined such that the element at (i, j) 
    is i * j (where 1 <= i <= m and 1 <= j <= n).

    Args:
        m: The number of rows in the multiplication table.
        n: The number of columns in the multiplication table.
        k: The rank of the number to find (1-indexed).

    Returns:
        The kth smallest number in the table.

    Examples:
        >>> solve(3, 3, 5)
        5
        >>> solve(2, 3, 4)
        4
    """

    def count_less_equal(target: int, rows: int, cols: int) -> int:
        """
        Counts how many numbers in the m x n table are less than or equal to target.
        
        For each row i, the numbers are i*1, i*2, ..., i*cols.
        The number of elements in row i such that i*j <= target is min(cols, target // i).
        """
        count = 0
        for i in range(1, rows + 1):
            # The largest j such that i * j <= target is floor(target / i)
            # We must also ensure j does not exceed the number of columns
            count += min(cols, target // i)
        return count

    # The range of possible values in the table is [1, m * n]
    low = 1
    high = m * n
    result = high

    # Binary search on the answer (the value itself)
    while low <= high:
        mid = (low + high) // 2
        
        # If the number of elements <= mid is at least k, 
        # then the kth smallest number is mid or something smaller.
        if count_less_equal(mid, m, n) >= k:
            result = mid
            high = mid - 1
        else:
            # Otherwise, the kth smallest number must be larger than mid.
            low = mid + 1

    return result
