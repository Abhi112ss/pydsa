METADATA = {
    "id": 649,
    "name": "Dota2 Senate",
    "slug": "dota2-senate",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "queue", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Simulate a voting process where senators ban each other based on their turn order.",
}

from collections import deque

def solve(senate: list[str]) -> str:
    """
    Simulates the Dota2 Senate voting process using a greedy approach with two queues.

    The strategy is to have each senator ban the next available opponent in the 
    voting order to prevent them from taking their turn.

    Args:
        senate: A list of strings where each string is either "Radiant" or "Dire".

    Returns:
        A string representing the winning faction ("Radiant" or "Dire").

    Examples:
        >>> solve(["Radiant", "Dire", "Radiant"])
        'Radiant'
        >>> solve(["r", "d", "r", "d"])
        'Radiant'
        >>> solve(["d", "r", "r"])
        'Radiant'
    """
    # Queues to store the indices of active senators for each faction
    radiant_indices = deque()
    dire_indices = deque()
    
    n = len(senate)
    
    # Initialize queues with the indices of the senators
    for index, faction in enumerate(senate):
        if faction == "Radiant" or faction == "r":
            radiant_indices.append(index)
        else:
            dire_indices.append(index)
            
    # Simulate the rounds until one faction is completely eliminated
    while radiant_indices and dire_indices:
        r_idx = radiant_indices.popleft()
        d_idx = dire_indices.popleft()
        
        # The senator with the smaller index acts first and bans the other.
        # The winner is re-added to their queue with an index offset (n) 
        # to represent their turn in the next round.
        if r_idx < d_idx:
            radiant_indices.append(r_idx + n)
        else:
            dire_indices.append(d_idx + n)
            
    return "Radiant" if radiant_indices else "Dire"
