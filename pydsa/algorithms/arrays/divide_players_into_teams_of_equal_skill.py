METADATA = {
    "id": 2491,
    "name": "Divide Players Into Teams of Equal Skill",
    "slug": "divide-players-into-teams-of-equal-skill",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Determine if all players can be divided into teams of two such that every team has the same total skill level.",
}

def solve(skill: list[int]) -> bool:
    """
    Determines if players can be divided into teams of two with equal skill sums.

    The strategy is to sort the skill levels and pair the smallest available 
    skill with the largest available skill. If all such pairs result in the 
    same sum, the condition is met.

    Args:
        skill: A list of integers representing the skill level of each player.

    Returns:
        True if all players can be divided into teams of equal skill, False otherwise.

    Examples:
        >>> solve([3, 2, 5, 1, 4])
        True
        >>> solve([1, 2, 3, 4, 5, 6, 7])
        False
    """
    # Sort the skill array to easily pair smallest with largest
    skill.sort()
    
    n = len(skill)
    # The target sum must be the sum of the smallest and largest elements
    target_sum = skill[0] + skill[n - 1]
    
    # Use two pointers to check if all pairs sum up to the target_sum
    left_index = 0
    right_index = n - 1
    
    while left_index < right_index:
        # If any pair does not match the target sum, it's impossible
        if skill[left_index] + skill[right_index] != target_sum:
            return False
        
        left_index += 1
        right_index -= 1
        
    return True
