METADATA = {
    "id": 1792,
    "name": "Maximum Average Pass Ratio",
    "slug": "maximum-average-pass-ratio",
    "category": "Heap",
    "aliases": [],
    "tags": ["heaps", "greedy", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Distribute extra students to classes to maximize the overall average pass ratio using a greedy approach with a max-priority queue.",
}

import heapq

def solve(classes: list[list[int]], extraStudents: int) -> float:
    """
    Calculates the maximum possible average pass ratio after distributing extra students.

    The strategy is to use a max-priority queue to greedily assign each extra student 
    to the class that provides the maximum incremental gain in the pass ratio.

    Args:
        classes: A list of lists where classes[i] = [pass_i, total_i].
        extraStudents: The number of additional students to distribute.

    Returns:
        The maximum possible average pass ratio as a float.

    Examples:
        >>> solve([[1, 2], [3, 5], [2, 2]], 2)
        0.7833333333333333
        >>> solve([[1, 2], [3, 5], [2, 2]], 3)
        0.8000000000000001
    """

    def calculate_gain(pass_count: int, total_count: int) -> float:
        """Calculates the marginal gain in pass ratio if one student is added."""
        current_ratio = pass_count / total_count
        new_ratio = (pass_count + 1) / (total_count + 1)
        return new_ratio - current_ratio

    # Max-heap stores (-gain, pass_count, total_count)
    # Python's heapq is a min-heap, so we negate the gain to simulate a max-heap.
    max_heap = []
    for pass_count, total_count in classes:
        gain = calculate_gain(pass_count, total_count)
        heapq.heappush(max_heap, (-gain, pass_count, total_count))

    # Greedily assign each extra student to the class with the highest gain
    for _ in range(extraStudents):
        neg_gain, pass_count, total_count = heapq.heappop(max_heap)
        
        # Update the class counts
        new_pass_count = pass_count + 1
        new_total_count = total_count + 1
        
        # Re-calculate the gain for this class and push back into heap
        new_gain = calculate_gain(new_pass_count, new_total_count)
        heapq.heappush(max_heap, (-new_gain, new_pass_count, new_total_count))

    # Calculate the final average pass ratio
    total_ratio_sum = 0.0
    for _, pass_count, total_count in max_heap:
        total_ratio_sum += pass_count / total_count

    return total_ratio_sum / len(classes)
