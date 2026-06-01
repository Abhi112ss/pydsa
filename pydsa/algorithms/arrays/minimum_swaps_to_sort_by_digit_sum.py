METADATA = {
    "id": 3551,
    "name": "Minimum Swaps to Sort by Digit Sum",
    "slug": "minimum-swaps-to-sort-by-digit-sum",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "permutation", "cycle decomposition"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of swaps required to sort an array based on the sum of the digits of its elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of swaps required to sort the array based 
    on the sum of the digits of each number.

    The problem is equivalent to finding the number of elements minus the 
    number of cycles in the permutation required to reach the sorted state.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of swaps required.

    Examples:
        >>> solve([12, 3, 21])
        1
        # Digit sums: [3, 3, 3]. If sums are equal, original order is preserved.
        # Wait, if sums are equal, the problem implies stable sorting or 
        # specific tie-breaking. Standard interpretation: sort by (sum, value).
    """
    def get_digit_sum(n: int) -> int:
        s = 0
        n = abs(n)
        while n:
            s += n % 10
            n //= 10
        return s

    n = len(nums)
    # Create a list of tuples: (digit_sum, original_value, original_index)
    # We include original_index to handle stable sorting if needed, 
    # though the problem usually implies sorting by (sum, value).
    indexed_elements = []
    for i in range(n):
        val = nums[i]
        indexed_elements.append((get_digit_sum(val), val, i))

    # Sort based on digit sum, then by the value itself to ensure a deterministic target
    indexed_elements.sort()

    # visited array to keep track of elements processed in cycle decomposition
    visited = [False] * n
    swaps = 0

    for i in range(n):
        # If already visited or already in the correct position, skip
        if visited[i] or indexed_elements[i][2] == i:
            continue

        # Find the size of the cycle
        cycle_size = 0
        current_idx = i
        while not visited[current_idx]:
            visited[current_idx] = True
            # Move to the index where the current element should have been
            # The element at indexed_elements[current_idx] belongs at its original index
            # But we want to know where the element currently at 'i' should go.
            # Actually, the standard cycle decomposition for swaps:
            # The element at index 'i' in the sorted array came from 'indexed_elements[i][2]'
            current_idx = indexed_elements[current_idx][2]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += (cycle_size - 1)

    return swaps
