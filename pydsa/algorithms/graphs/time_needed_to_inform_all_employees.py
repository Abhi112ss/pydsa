METADATA = {
    "id": 1376,
    "name": "Time Needed to Inform All Employees",
    "slug": "time-needed-to-inform-all-employees",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "trees", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum time required to inform all employees in a hierarchy given notification times.",
}

def solve(manager_id: int, announcement_time: list[int], adjacency_list: list[list[int]]) -> int:
    """
    Calculates the total time required for a manager to inform all employees in a tree structure.

    The problem is equivalent to finding the longest path from the root to any leaf,
    where the path weight is the sum of announcement times of the nodes along the path.

    Args:
        manager_id: The ID of the manager who starts the announcement.
        announcement_time: A list where announcement_time[i] is the time taken by 
            employee i to inform all their direct subordinates.
        adjacency_list: A list of lists representing the tree structure where 
            adjacency_list[i] contains the IDs of direct subordinates of employee i.

    Returns:
        The total time taken to inform all employees.

    Examples:
        >>> solve(0, [3, 3, 3], [[1, 2], [], []])
        3
        >>> solve(0, [3, 2, 3, 3], [[1, 2], [3], [4], [], []])
        8
    """
    
    def get_max_time_from_node(current_employee: int) -> int:
        """
        Recursive helper to find the maximum time required to inform all descendants.
        """
        # Base case: if the employee has no subordinates, no additional time is needed
        if not adjacency_list[current_employee]:
            return 0
        
        max_subordinate_time = 0
        
        # Explore all direct subordinates
        for subordinate in adjacency_list[current_employee]:
            # The time for this branch is the time the current employee takes 
            # plus the time the subordinate takes to inform their own subtree
            time_for_branch = get_max_time_from_node(subordinate)
            max_subordinate_time = max(max_subordinate_time, time_for_branch)
            
        # Total time for this node is its own announcement time + max time of its branches
        return announcement_time[current_employee] + max_subordinate_time

    # The total time is the maximum time path starting from the initial manager
    return get_max_time_from_node(manager_id)
