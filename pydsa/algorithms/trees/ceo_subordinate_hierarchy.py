METADATA = {
    "id": 3236,
    "name": "CEO Subordinate Hierarchy",
    "slug": "ceo_subordinate_hierarchy",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine the hierarchical structure and relationships within a company starting from a CEO.",
}

from collections import defaultdict

def solve(n: int, relations: list[list[int]]) -> list[int]:
    """
    Computes the hierarchical level of each employee in a company.

    The hierarchy is represented as a directed tree where the CEO is at level 0,
    and each subordinate is at a level exactly one greater than their manager.

    Args:
        n: The total number of employees.
        relations: A list of pairs [manager_id, subordinate_id] representing 
                   the reporting structure.

    Returns:
        A list of integers where the i-th element is the level of employee i.

    Examples:
        >>> solve(3, [[0, 1], [0, 2]])
        [0, 1, 1]
        >>> solve(4, [[0, 1], [1, 2], [1, 3]])
        [0, 1, 2, 2]
    """
    # Build an adjacency list to represent the tree structure
    # Each key is a manager, and the value is a list of their direct subordinates
    adj = defaultdict(list)
    has_manager = [False] * n
    
    for manager, subordinate in relations:
        adj[manager].append(subordinate)
        has_manager[subordinate] = True
        
    # The CEO is the node that does not have a manager
    ceo_id = -1
    for i in range(n):
        if not has_manager[i]:
            ceo_id = i
            break
            
    # levels array to store the depth of each employee
    levels = [0] * n
    
    # Use iterative DFS (or BFS) to traverse the tree and assign levels
    # Stack stores tuples of (current_employee, current_level)
    stack = [(ceo_id, 0)]
    
    while stack:
        current_node, current_level = stack.pop()
        levels[current_node] = current_level
        
        # Traverse all subordinates and increment the level
        for subordinate in adj[current_node]:
            stack.append((subordinate, current_level + 1))
            
    return levels
