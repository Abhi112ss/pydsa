METADATA = {
    "id": 781,
    "name": "Rabbits in Forest",
    "slug": "rabbits-in-forest",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum number of rabbits in a forest given their answers about how many others share their color.",
}

def solve(rabbits: list[int]) -> int:
    """
    Calculates the minimum number of rabbits in the forest.

    Each rabbit's answer 'x' implies there are x other rabbits of the same color,
    meaning a group of size (x + 1) exists. We group rabbits by their answers
    to minimize the total count.

    Args:
        rabbits: A list of integers where each integer represents the number
                 of other rabbits of the same color reported by a rabbit.

    Returns:
        The minimum total number of rabbits in the forest.

    Examples:
        >>> solve([1, 1, 2])
        3
        >>> solve([10])
        11
        >>> solve([1, 1, 1])
        4
    """
    # Map to store the frequency of each reported answer
    # key: number of other rabbits (x), value: count of rabbits who gave that answer
    answer_counts: dict[int, int] = {}
    
    for answer in rabbits:
        answer_counts[answer] = answer_counts.get(answer, 0) + 1
        
    total_rabbits = 0
    
    for answer, count in answer_counts.items():
        # A group of rabbits who all say 'answer' can have at most (answer + 1) members.
        # For example, if answer is 2, a group can have 3 rabbits.
        group_capacity = answer + 1
        
        # Calculate how many full groups of size (answer + 1) are needed to cover 'count' rabbits.
        # We use ceiling division: (count + group_capacity - 1) // group_capacity
        num_groups = (count + group_capacity - 1) // group_capacity
        
        # Each group must contain exactly (answer + 1) rabbits to satisfy the minimum requirement.
        total_rabbits += num_groups * group_capacity
        
    return total_rabbits
