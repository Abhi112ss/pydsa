METADATA = {
    "id": 1600,
    "name": "Throne Inheritance",
    "slug": "throne-inheritance",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the person who will inherit the throne by counting all descendants of a given person in a family tree.",
}

def solve(people: list[list[int]], target: int) -> int:
    """
    Finds the person who will inherit the throne after the target person.

    The inheritance follows a rule where a person's descendants (children, 
    grandchildren, etc.) are listed in order of their generation and then 
    by their index in the input list.

    Args:
        people: A list of lists where people[i] contains the children of person i.
        target: The ID of the person currently on the throne.

    Returns:
        The ID of the person who will inherit the throne.

    Examples:
        >>> solve([[1, 2, 3], [], [], []], 0)
        1
        >>> solve([[1, 2, 3], [], [], []], 1)
        1
        >>> solve([[1, 2, 3], [4], [], [], []], 0)
        1
    """
    # The problem asks for the first descendant in a level-order traversal.
    # A Breadth-First Search (BFS) is ideal for finding the "next" person 
    # in terms of generational order.
    
    queue: list[int] = [target]
    visited_count: int = 0
    
    # We use a simple pointer-based queue to avoid O(n) pop(0) operations
    head: int = 0
    
    while head < len(queue):
        current_person = queue[head]
        head += 1
        
        # If we encounter the target person, we don't count them as their own 
        # successor in the context of "descendants", but the problem logic 
        # implies we look for the first person in the BFS queue after the target.
        # However, the standard BFS approach starting from target will 
        # naturally put the first child at the front of the queue.
        
        # If we are at the target, we don't increment the count for the 
        # 'successor' yet, we just add children. 
        # Actually, a simpler way: The first person added to the queue 
        # AFTER the target is the successor.
        
        if current_person == target:
            # Add all children of the target to the queue
            for child in people[current_person]:
                queue.append(child)
        else:
            # If we have already started collecting descendants, 
            # the very first descendant we encounter is the answer.
            return current_person

    # If the target has no descendants, the target inherits their own throne.
    return target

# Note: The logic above is slightly simplified. Let's refine the BFS 
# to strictly follow the requirement: "The first person in the 
# level-order traversal of the target's descendants".

def solve_refined(people: list[list[int]], target: int) -> int:
    """
    Finds the person who will inherit the throne using a BFS approach.
    """
    # Queue for BFS
    queue: list[int] = [target]
    
    # Pointer for the queue to simulate efficient popping
    head: int = 0
    
    # We need to find the first person in the BFS traversal that is NOT the target.
    # Since the target is the root of our BFS, the first person we pull 
    # from the queue that isn't the target is the immediate successor.
    
    while head < len(queue):
        current = queue[head]
        head += 1
        
        # If this is the target, we add its children to the queue.
        # We don't return the target because the target cannot be their own successor
        # unless they have no descendants.
        if current == target:
            for child in people[current]:
                queue.append(child)
        else:
            # The first person we encounter that is not the target 
            # is the first descendant in level-order.
            return current
            
    # If the loop finishes without returning, the target has no descendants.
    return target

# Re-assigning to the required function name
solve = solve_refined