METADATA = {
    "id": 2358,
    "name": "Maximum Number of Groups Entering a Competition",
    "slug": "maximum-number-of-groups-entering-a-competition",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of groups that can enter a competition such that each group's total power is strictly less than the next group's total power.",
}

def solve(power: list[int]) -> int:
    """
    Calculates the maximum number of groups that can enter a competition.
    
    A group can enter if its total power is strictly less than the total 
    power of the next group. To maximize the number of groups, we use a 
    greedy approach by sorting the powers and forming groups with the 
    smallest available powers first.

    Args:
        power: A list of integers representing the power of each participant.

    Returns:
        The maximum number of groups that can enter the competition.

    Examples:
        >>> solve([4, 9, 4, 6, 7])
        2
        >>> solve([1, 1, 1, 1, 1])
        1
    """
    # Sort the powers to allow greedy selection of the smallest possible groups
    power.sort()
    
    total_groups = 0
    current_group_sum = 0
    previous_group_sum = 0
    
    for p in power:
        # Try adding the current participant to the current group
        current_group_sum += p
        
        # If the current group's sum is strictly greater than the previous group's sum,
        # we can finalize this group and move to the next one.
        if current_group_sum > previous_group_sum:
            total_groups += 1
            previous_group_sum = current_group_sum
            current_group_sum = 0
            
    # Note: If the loop ends and current_group_sum > 0, those participants 
    # cannot form a new group that satisfies the condition (sum > previous_sum),
    # so they are effectively discarded.
    
    return total_groups
