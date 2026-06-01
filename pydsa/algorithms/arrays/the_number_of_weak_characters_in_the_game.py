METADATA = {
    "id": 1996,
    "name": "The Number of Weak Characters in the Game",
    "slug": "the-number-of-weak-characters-in-the-game",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count characters that are strictly weaker than another character in both attack and health.",
}

def solve(attack: list[int], health: list[int]) -> int:
    """
    Counts the number of weak characters in the game.
    
    A character is weak if there exists another character with both 
    strictly greater attack and strictly greater health.

    Args:
        attack: A list of integers representing the attack of each character.
        health: A list of integers representing the health of each character.

    Returns:
        The total number of weak characters.

    Examples:
        >>> solve([5, 1, 5, 5], [6, 2, 1, 3])
        1
        >>> solve([10, 10, 10], [10, 10, 10])
        0
    """
    n = len(attack)
    if n == 0:
        return 0

    # Combine attack and health into pairs for sorting
    characters = []
    for i in range(n):
        characters.append((attack[i], health[i]))

    # Sort characters:
    # 1. Attack descending: This ensures that for any character at index i, 
    #    all characters at index j < i have attack[j] >= attack[i].
    # 2. Health ascending: For characters with the same attack, sorting health 
    #    ascending ensures that a character cannot be "weaker" than another 
    #    with the same attack (since we need strictly greater attack).
    characters.sort(key=lambda x: (-x[0], x[1]))

    weak_count = 0
    max_health_seen = 0

    # Iterate through the sorted characters.
    # Because of the sorting strategy, we only need to track the maximum 
    # health seen so far to determine if the current character is weak.
    # Since attack is descending, any character seen before has attack >= current.
    # Because we sorted same-attack characters by ascending health, 
    # max_health_seen will only be greater than current health if the 
    # previous character had a strictly greater attack.
    for _, current_health in characters:
        if current_health < max_health_seen:
            weak_count += 1
        else:
            # Update the maximum health encountered so far
            max_health_seen = current_health

    return weak_count
