METADATA = {
    "id": 2244,
    "name": "Minimum Rounds to Complete All Tasks",
    "slug": "minimum-rounds-to-complete-all-tasks",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of rounds to complete all tasks given that each round can complete either 2 or 3 tasks.",
}

def solve(tasks: list[int]) -> int:
    """
    Calculates the minimum number of rounds to complete all tasks.
    
    Each round can complete either exactly 2 tasks or exactly 3 tasks.
    If a task group cannot be divided into groups of 2 or 3, it's impossible.

    Args:
        tasks: A list of integers where each integer represents a group of tasks.

    Returns:
        The minimum number of rounds required, or -1 if it's impossible.

    Examples:
        >>> solve([2, 3, 3, 4, 5])
        5
        >>> solve([1])
        -1
        >>> solve([3, 6, 7, 10])
        4
    """
    total_rounds = 0
    
    for count in tasks:
        # A group of 1 task cannot be completed using rounds of 2 or 3
        if count == 1:
            return -1
        
        # Mathematical insight:
        # To minimize rounds, we want to maximize the number of 3-task rounds.
        # If count % 3 == 0: rounds = count // 3
        # If count % 3 == 1: (e.g., 4) we use two 2-task rounds (4 = 2 + 2). 
        #                   This is equivalent to (count // 3) + 1.
        # If count % 3 == 2: (e.g., 5) we use one 3-task and one 2-task round (5 = 3 + 2).
        #                   This is equivalent to (count // 3) + 1.
        # In all valid cases (count > 1), the formula is ceil(count / 3).
        
        # Using integer arithmetic for ceil(count / 3):
        total_rounds += (count + 2) // 3
        
    return total_rounds
