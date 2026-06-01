METADATA = {
    "id": 2576,
    "name": "Find the Maximum Number of Marked Indices",
    "slug": "find-the-maximum-number-of-marked-indices",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of marked indices such that no two marked indices are within distance 2 of each other and no marked index is within distance 2 of an unmarked index.",
}

def solve(n: int, indices: list[list[int]]) -> int:
    """
    Args:
        n: The total number of indices.
        indices: A list of lists where each sublist contains [index, value].

    Returns:
        The maximum number of indices that can be marked.
    """
    sorted_indices = sorted(indices)
    
    left_marked = []
    last_marked_pos = -3
    for index, value in sorted_indices:
        if value == 1:
            if index - last_marked_pos >= 3:
                left_marked.append(index)
                last_marked_pos = index
                
    right_marked = []
    last_marked_pos = n + 3
    for index, value in reversed(sorted_indices):
        if value == 1:
            if last_marked_pos - index >= 3:
                right_marked.append(index)
                last_marked_pos = index
                
    if not left_marked or not right_marked:
        return len(left_marked) + len(right_marked)
        
    left_count = len(left_marked)
    right_count = len(right_marked)
    
    if left_marked[-1] < right_marked[0] - 2:
        return left_count + right_count
    else:
        return max(left_count, right_count)