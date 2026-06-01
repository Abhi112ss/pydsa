METADATA = {
    "id": 163,
    "name": "Missing Ranges",
    "slug": "missing-ranges",
    "category": "arrays",
    "aliases": [],
    "tags": ["arrays", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest sorted list of ranges that cover every missing number in a sorted integer array.",
}

def solve(nums: list[int], lower: int, upper: int) -> list[str]:
    """
    Finds the smallest sorted list of ranges that cover every missing number in the sorted integer array `nums`
    between `lower` and `upper`.

    Args:
        nums: A sorted list of integers.
        lower: The lower bound of the range to check.
        upper: The upper bound of the range to check.

    Returns:
        A list of strings representing the missing ranges. Each range is either "a" for a single number
        or "a->b" for a range of numbers.

    Examples:
        >>> solve([0, 1, 3, 50, 75], 0, 99)
        ["2", "4->49", "51->74", "76->99"]
        >>> solve([-1], -1, -1)
        []
        >>> solve([], 1, 1)
        ["1"]
    """
    result = []
    next_expected = lower
    
    for num in nums:
        # If there's a gap between next_expected and current number
        if next_expected < num:
            # Add the missing range from next_expected to num-1
            start = next_expected
            end = num - 1
            if start == end:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{end}")
        # Update next_expected to be the next number after current
        next_expected = num + 1
        # If next_expected exceeds upper, we can break early
        if next_expected > upper:
            break
    
    # After processing all numbers, check if there's still a gap to upper
    if next_expected <= upper:
        start = next_expected
        end = upper
        if start == end:
            result.append(f"{start}")
        else:
            result.append(f"{start}->{end}")
    
    return result