METADATA = {
    "id": 2164,
    "name": "Sort Even and Odd Indices Independently",
    "slug": "sort-even-and-odd-indices-independently",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort the elements at even indices and odd indices of an array independently.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Sorts the elements at even indices and odd indices of the input list independently.

    Args:
        nums: A list of integers.

    Returns:
        A new list where even-indexed elements are sorted and odd-indexed 
        elements are sorted, maintaining their original index parity.

    Examples:
        >>> solve([4, 1, 2, 3])
        [2, 1, 4, 3]
        >>> solve([5, 4, 3, 2, 1])
        [3, 2, 5, 4, 1]
    """
    n = len(nums)
    if n <= 1:
        return nums[:]

    # Extract elements at even and odd positions
    even_elements = [nums[i] for i in range(0, n, 2)]
    odd_elements = [nums[i] for i in range(1, n, 2)]

    # Sort both lists independently
    even_elements.sort()
    odd_elements.sort()

    # Reconstruct the result list
    result = [0] * n
    even_ptr = 0
    odd_ptr = 0

    for i in range(n):
        if i % 2 == 0:
            # Place the next smallest even-indexed element
            result[i] = even_elements[even_ptr]
            even_ptr += 1
        else:
            # Place the next smallest odd-indexed element
            result[i] = odd_elements[odd_ptr]
            odd_ptr += 1

    return result
