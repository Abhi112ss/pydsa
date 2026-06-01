METADATA = {
    "id": 1439,
    "name": "Find the Kth Smallest Sum of a Matrix With Sorted Rows",
    "slug": "find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows",
    "category": "Heap",
    "aliases": [],
    "tags": ["heaps", "priority_queue", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(m * k log k)",
    "space_complexity": "O(k)",
    "description": "Find the kth smallest sum of elements formed by picking one element from each row of a matrix where each row is sorted.",
}

import heapq

def solve(mat: list[list[int]], k: int) -> int:
    """
    Finds the kth smallest sum of elements formed by picking one element from each row.

    The algorithm works by iteratively merging the current set of smallest sums 
    with the next row. For each merge, we use a min-heap to find the k smallest 
    possible sums between the existing sums and the elements of the new row.

    Args:
        mat: A 2D list of integers where each row is sorted in non-decreasing order.
        k: The target rank of the sum to find.

    Returns:
        The kth smallest sum.

    Examples:
        >>> solve([[1,3,5],[2,4,6]], 3)
        6
        >>> solve([[1,10,10],[1,4,5],[2,3,6]], 7)
        7
    """
    # Initialize current_sums with the first row, limited to the first k elements
    # since we only ever care about the k smallest sums.
    current_sums = mat[0][:k]

    for row_index in range(1, len(mat)):
        next_row = mat[row_index]
        min_heap = []
        
        # We want to find the k smallest sums from (current_sums[i] + next_row[j])
        # To do this efficiently, we treat this as merging sorted lists or 
        # finding k smallest pairs.
        # We use a min-heap to store (sum, index_in_next_row) for each element in current_sums.
        for s in current_sums:
            # Push (sum, index_in_next_row)
            # We start with the smallest element in the next row for every sum in current_sums
            heapq.heappush(min_heap, (s + next_row[0], 0, s))

        new_sums = []
        # Extract up to k smallest sums from the heap
        while min_heap and len(new_sums) < k:
            current_sum, row_idx, original_s = heapq.heappop(min_heap)
            new_sums.append(current_sum)

            # If there is a next element in the current row, push the next possible sum
            if row_idx + 1 < len(next_row):
                heapq.heappush(min_heap, (original_s + next_row[row_idx + 1], row_idx + 1, original_s))
        
        current_sums = new_sums

    return current_sums[k - 1]
