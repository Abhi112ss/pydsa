METADATA = {
    "id": 544,
    "name": "Output Contest Matches",
    "slug": "output-contest-matches",
    "category": "Simulation",
    "aliases": [],
    "tags": ["recursion", "simulation", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n log n)",
    "description": "Simulate a tournament where the strongest team plays the weakest team in each round.",
}

def solve(teams: list[int]) -> list[list[int]]:
    """
    Simulates a tournament where in each round, the strongest remaining team 
    is paired with the weakest remaining team.

    Args:
        teams: A list of integers representing the skill levels of the teams.

    Returns:
        A list of lists, where each inner list contains two teams that played 
        against each other in a specific round.

    Examples:
        >>> solve([1, 2, 3, 4])
        [[1, 4], [2, 3]]
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8])
        [[1, 8], [2, 7], [3, 6], [4, 5]]
    """
    # Sort teams to easily pick the strongest and weakest
    sorted_teams = sorted(teams)
    matches = []
    
    left_index = 0
    right_index = len(sorted_teams) - 1
    
    # Continue pairing until the pointers meet or cross
    while left_index < right_index:
        # Pair the weakest (left) with the strongest (right)
        matches.append([sorted_teams[left_index], sorted_teams[right_index]])
        
        # Move pointers inward to simulate the removal of these teams
        left_index += 1
        right_index -= 1
        
    return matches
