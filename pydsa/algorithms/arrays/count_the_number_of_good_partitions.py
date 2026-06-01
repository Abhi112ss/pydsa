METADATA = {
    "id": 2963,
    "name": "Count the Number of Good Partitions",
    "slug": "count-the-number-of-good-partitions",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "greedy", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of ways to partition an array such that each partition contains all occurrences of any element present within it.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of good partitions of an array.
    
    A partition is good if for every element in the partition, all its 
    occurrences in the original array are also within that same partition.

    Args:
        nums: A list of integers.

    Returns:
        The number of ways to partition the array into good partitions.

    Examples:
        >>> solve([1, 3, 2, 2, 3, 1])
        2
        >>> solve([1, 1, 1, 1])
        1
        >>> solve([1, 2, 3, 4])
        4
    """
    if not nums:
        return 0

    # Step 1: Map each number to its first and last occurrence index
    first_occurrence = {}
    last_occurrence = {}
    
    for index, value in enumerate(nums):
        if value not in first_occurrence:
            first_occurrence[value] = index
        last_occurrence[value] = index

    # Step 2: Create intervals [start, end] for each unique element
    intervals = []
    for value in first_occurrence:
        intervals.append([first_occurrence[value], last_occurrence[value]])

    # Step 3: Sort intervals by their start position to facilitate merging
    intervals.sort()

    # Step 4: Merge overlapping intervals to find disjoint "blocks"
    # Each disjoint block represents a mandatory group of elements that must stay together.
    num_blocks = 0
    if not intervals:
        return 0
        
    current_end = -1
    
    for start, end in intervals:
        # If the current interval starts after the current merged block ends,
        # it means we have completed a "good partition" block.
        if start > current_end:
            num_blocks += 1
            current_end = end
        else:
            # Otherwise, extend the current block to include this interval
            current_end = max(current_end, end)

    # Step 5: The number of ways to partition is 2^(number of blocks - 1)
    # Because if we have K disjoint blocks, we have K-1 "gaps" where we can 
    # choose to either split or not split.
    return pow(2, num_blocks - 1, 10**9 + 7)
