METADATA = {
    "id": 763,
    "name": "Partition Labels",
    "slug": "partition_labels",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Partition a string into as many parts as possible so that each letter appears in at most one part.",
}

def solve(s: str) -> list[int]:
    """
    Partitions the string into as many parts as possible such that each letter 
    appears in at most one part.

    Args:
        s: The input string to partition.

    Returns:
        A list of integers representing the sizes of the partitions.

    Examples:
        >>> solve("ababcbacadefegdehijhklij")
        [9, 7, 8]
        >>> solve("eccbbbbdec")
        [10]
    """
    # Step 1: Record the last occurrence index of every character in the string.
    # Since the input consists of lowercase English letters, the space is O(1).
    last_occurrence = {char: index for index, char in enumerate(s)}

    partition_sizes = []
    current_partition_start = 0
    current_partition_end = 0

    # Step 2: Iterate through the string to find partition boundaries.
    for current_index, char in enumerate(s):
        # Expand the current partition boundary to include the last occurrence 
        # of the current character.
        current_partition_end = max(current_partition_end, last_occurrence[char])

        # If the current index reaches the furthest last occurrence seen so far,
        # it means all characters within this range do not appear outside this range.
        if current_index == current_partition_end:
            size = current_index - current_partition_start + 1
            partition_sizes.append(size)
            # Move the start pointer to the beginning of the next potential partition.
            current_partition_start = current_index + 1

    return partition_sizes
