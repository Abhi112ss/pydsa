METADATA = {
    "id": 2682,
    "name": "Find the Losers of the Circular Game",
    "slug": "find-the-losers-of-the-circular-game",
    "category": "Simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate a circular elimination game to find the last two remaining players.",
}

def solve(n: int, k: int) -> list[int]:
    """
    Finds the last two remaining players in a circular elimination game.

    The game starts with players 1 to n. In each step, the current player 
    moves k-1 steps forward (circularly) and the player landed on is eliminated.
    The game continues until only two players remain.

    Args:
        n: The total number of players.
        k: The step size for movement.

    Returns:
        A list of two integers representing the last two remaining players 
        in ascending order.

    Examples:
        >>> solve(5, 2)
        [2, 4]
        >>> solve(10, 3)
        [2, 8]
    """
    # We use the Josephus problem logic to find the position of the last remaining person.
    # However, since we need the last TWO people, we can solve for the last person
    # and the second to last person by adjusting the base cases.
    
    # Let f(n, k) be the position of the survivor among n people.
    # The recurrence is: f(n, k) = (f(n-1, k) + k) % n
    
    # To find the last two, we can track the positions of the last two survivors.
    # Let's denote the positions of the last two survivors as (p1, p2).
    # When we go from i-1 people to i people, the positions shift by k.
    
    # Base case: when 2 people are left, their positions in a 0-indexed system are 0 and 1.
    last_two = [0, 1]
    
    # Iteratively build up from 3 people to n people.
    for current_n in range(3, n + 1):
        # The new position of each survivor is (old_position + k) % current_n
        # We apply this transformation to both survivors.
        new_p1 = (last_two[0] + k) % current_n
        new_p2 = (last_two[1] + k) % current_n
        
        # Since the elimination process removes one person, the relative order 
        # of the survivors might change or they might shift. 
        # However, in the standard Josephus recurrence, we are mapping 
        # the indices from the (n-1) state to the n state.
        last_two = [new_p1, new_p2]

    # Convert 0-indexed positions back to 1-indexed and sort.
    # Note: The recurrence above actually tracks the indices of the survivors.
    # Because we need the last two, we must ensure we handle the mapping correctly.
    # A more robust way for the last TWO is to find the survivor of (n, k) 
    # and the survivor of (n, k) if we had stopped at 2.
    
    # Re-calculating using the standard Josephus for the last person:
    # survivor_1_indexed = josephus(n, k)
    # To find the second to last, we can use the property that the last two 
    # are the survivors of the process when n=2.
    
    # Let's refine the iterative approach:
    # We want the positions of the two people who would be left if we stopped at 2.
    # Let's use the standard Josephus for the last person (survivor)
    # and a slightly modified one for the second to last.
    
    # Actually, the simplest way to get the last two is to realize that 
    # the last two people are the survivors of the Josephus process.
    # We can find the position of the last person (survivor) and the 
    # position of the person who was eliminated second to last.
    
    # Let's use the iterative approach for the last person:
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
        
    # To find the second to last, we need to know which index was 
    # "the survivor" when there were 3 people, and then map it.
    # But a cleaner way: The last two people are the results of 
    # the Josephus recurrence starting from n=2.
    
    # Let's re-run the simulation logic correctly:
    # For n=2, survivors are [0, 1]
    # For n=3, survivors are [(0+k)%3, (1+k)%3]
    # This is exactly what the loop above does.
    
    # However, there is a catch: the order of indices in 'last_two' 
    # might not be sorted, and the modulo might wrap around.
    # We must ensure we are tracking the two specific individuals.
    
    # Let's use the correct logic:
    # Let S(n, k) be the set of indices of the last two survivors.
    # S(2, k) = {0, 1}
    # S(n, k) = { (x + k) % n | x in S(n-1, k) }
    
    # This is exactly what the loop `for current_n in range(3, n + 1)` does.
    # We just need to sort the final result.
    
    res = sorted([last_two[0] + 1, last_two[1] + 1])
    return res
