METADATA = {
    "id": 457,
    "name": "Circular Array Loop",
    "slug": "circular-array-loop",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "cycle_detection"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if there is a cycle in a circular array where all elements in the cycle move in the same direction and the cycle length is greater than one.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if there is a cycle in the circular array.

    A cycle is valid if:
    1. All elements in the cycle move in the same direction (all positive or all negative).
    2. The cycle length is greater than one.

    Args:
        nums: A list of integers representing the jumps.

    Returns:
        True if a valid cycle exists, False otherwise.

    Examples:
        >>> solve([2, -1, 1, -2, 2])
        True
        >>> solve([-1, 2])
        False
    """
    n = len(nums)

    def get_next_index(current_index: int) -> int:
        """Calculates the next index in the circular array."""
        return (current_index + nums[current_index]) % n

    for i in range(n):
        # If nums[i] is 0, it means we've already visited this index and found no cycle
        if nums[i] == 0:
            continue

        slow = i
        fast = i
        
        # Direction of the current potential cycle
        is_forward = nums[i] > 0

        while True:
            # Move slow pointer one step
            prev_slow = slow
            slow = get_next_index(slow)
            
            # Check if slow pointer changed direction or hit a dead end
            if (nums[slow] > 0) != is_forward or nums[slow] == 0:
                break
            
            # Move fast pointer two steps
            # First step
            fast = get_next_index(fast)
            if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                break
            # Second step
            fast = get_next_index(fast)
            if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                break

            # If slow and fast meet, a cycle is detected
            if slow == fast:
                # Check if cycle length is > 1 (not a self-loop)
                if slow == get_next_index(slow):
                    break
                return True

        # Optimization: Mark all visited indices in this failed path as 0
        # to avoid re-processing them in the outer loop.
        curr = i
        while (nums[curr] > 0) == is_forward:
            next_idx = get_next_index(curr)
            # We use a temporary value to mark visited to avoid direction confusion
            # but for simplicity in this implementation, we just zero out the path.
            # However, to be safe with the direction check, we only zero if it matches.
            temp = nums[curr]
            nums[curr] = 0
            if next_idx == curr: # Self loop case
                break
            curr = next_idx
            if nums[curr] == 0:
                break

    return False
