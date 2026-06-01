METADATA = {
    "id": 1130,
    "name": "Minimum Cost Tree From Leaf Values",
    "slug": "minimum-cost-tree-from-leaf-values",
    "category": "Dynamic Programming / Greedy",
    "aliases": [],
    "tags": ["greedy", "monotonic_stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to build a tree from leaf values where the cost is the sum of the products of non-leaf nodes.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the minimum cost to build a tree from leaf values using a monotonic stack.

    The problem can be viewed as repeatedly removing the smallest element and 
    multiplying it by its smaller neighbor to minimize the total cost. This is 
    equivalent to finding the local minimums in a monotonic decreasing stack.

    Args:
        arr: A list of integers representing the leaf values in order.

    Returns:
        The minimum total cost of the tree.

    Examples:
        >>> solve([6, 2, 4])
        24
        >>> solve([2, 4, 3])
        12
    """
    # We use a monotonic decreasing stack to simulate the process of 
    # merging the smallest available leaf with its smaller neighbor.
    # We add a sentinel value (infinity) to ensure all elements are processed.
    stack: list[int] = [float('inf')]
    total_cost: int = 0

    for value in arr:
        # When we encounter a value larger than the top of the stack, 
        # the top of the stack is a local minimum.
        while stack[-1] <= value:
            mid = stack.pop()
            # The cost of removing 'mid' is the product of 'mid' and 
            # the smaller of its two neighbors (the new stack top or the current value).
            neighbor = min(stack[-1], value)
            total_cost += mid * neighbor
        
        stack.append(value)

    # After the loop, the stack contains elements in strictly decreasing order.
    # We process the remaining elements by merging them from the end.
    while len(stack) > 2:
        mid = stack.pop()
        total_cost += mid * stack[-1]

    return int(total_cost)
