METADATA = {
    "id": 3482,
    "name": "Analyze Organization Hierarchy",
    "slug": "analyze_organization_hierarchy",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "dfs", "bfs", "adjacency list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Analyze an organization hierarchy to determine properties like depth, level counts, or specific node relationships using tree traversal.",
}

from typing import Optional, Dict, List


class OrganizationNode:
    """Represents a node in the organization hierarchy."""

    def __init__(self, employee_id: int, name: str):
        self.employee_id = employee_id
        self.name = name
        self.subordinates: List["OrganizationNode"] = []


def solve(employees: List[Dict[str, any]], relations: List[List[int]]) -> Dict[str, any]:
    """
    Analyzes the organization hierarchy to calculate depth and level distribution.

    Args:
        employees: A list of dictionaries where each dict contains 'id' and 'name'.
        relations: A list of pairs [manager_id, subordinate_id].

    Returns:
        A dictionary containing:
            - 'max_depth': The maximum depth of the hierarchy (root is depth 1).
            - 'level_counts': A dictionary mapping depth to number of employees at that depth.
            - 'root_id': The ID of the top-level manager.

    Examples:
        >>> employees = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
        >>> relations = [[1, 2], [1, 3]]
        >>> solve(employees, relations)
        {'max_depth': 2, 'level_counts': {1: 1, 2: 2}, 'root_id': 1}
    """
    if not employees:
        return {"max_depth": 0, "level_counts": {}, "root_id": None}

    # Map ID to Node object for O(1) access
    id_to_node: Dict[int, OrganizationNode] = {}
    for emp in employees:
        id_to_node[emp["id"]] = OrganizationNode(emp["id"], emp["name"])

    # Track children and parents to find the root
    adj: Dict[int, List[int]] = {emp["id"]: [] for emp in employees}
    has_parent: Dict[int, bool] = {emp["id"]: False for emp in employees}

    for manager_id, sub_id in relations:
        adj[manager_id].append(sub_id)
        has_parent[sub_id] = True

    # The root is the node that has no parent
    root_id: Optional[int] = None
    for emp_id, parent_exists in has_parent.items():
        if not parent_exists:
            root_id = emp_id
            break

    if root_id is None:
        # This case handles cycles or empty hierarchies if input is invalid
        return {"max_depth": 0, "level_counts": {}, "root_id": None}

    level_counts: Dict[int, int] = {}
    max_depth = 0

    # Iterative DFS to avoid recursion depth issues in large hierarchies
    # Stack stores tuples of (current_node_id, current_depth)
    stack: List[tuple[int, int]] = [(root_id, 1)]

    while stack:
        curr_id, depth = stack.pop()
        
        # Update depth metrics
        max_depth = max(max_depth, depth)
        level_counts[depth] = level_counts.get(depth, 0) + 1

        # Add subordinates to stack for traversal
        for sub_id in adj[curr_id]:
            stack.append((sub_id, depth + 1))

    return {
        "max_depth": max_depth,
        "level_counts": dict(sorted(level_counts.items())),
        "root_id": root_id,
    }
