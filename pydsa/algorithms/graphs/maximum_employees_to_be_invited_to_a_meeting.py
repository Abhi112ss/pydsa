METADATA = {
    "id": 2127,
    "name": "Maximum Employees to Be Invited to a Meeting",
    "slug": "maximum-employees-to-be-invited-to-a-meeting",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "dfs", "cycle_detection", "functional_graph"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of employees that can be invited to a meeting given their preference constraints.",
}

def solve(invitations: list[list[int]]) -> int:
    """
    Calculates the maximum number of employees that can be invited to a meeting.
    
    The problem describes a functional graph where each node has exactly one outgoing edge.
    In such a graph, each connected component contains exactly one cycle.
    The maximum number of employees can be formed in two ways:
    1. A single cycle (all nodes in the cycle).
    2. Two separate cycles connected by a path (the path is traversed twice, 
       effectively meaning we pick two cycles and the path between them).
       Wait, the rule is: we can pick two cycles if they are disjoint and 
       connected by a path, but we can only visit the path once. 
       Actually, the optimal structure is either:
       - A single cycle.
       - Two cycles connected by a path (the path is traversed twice, 
         but the problem allows us to pick two cycles and the path between them 
         if we can visit them. However, in a functional graph, two cycles 
         cannot be connected by a path in a way that allows visiting both 
         without repeating nodes unless they are part of the same component. 
         In a functional graph, each component has exactly one cycle. 
         Therefore, we can pick two separate components, each containing a cycle, 
         and the total is the sum of the sizes of the two largest cycles.
         Wait, the rule is: we can pick two cycles if they are in different components.
         If they are in the same component, we can only pick one cycle or a cycle 
         plus a path leading into it.
         Actually, the correct logic for functional graphs:
         - Case 1: A single cycle.
         - Case 2: Two separate cycles from different components.
         - Case 3: A cycle and a path leading into it (this is just a cycle).
         Wait, the actual rule for this specific problem:
         You can pick two cycles if they are in different components.
         If you pick two cycles, you can't pick any paths between them because 
         the path would be traversed twice.
         Actually, the maximum is:
         max(max_cycle_size_in_one_component, sum_of_two_largest_cycles_from_different_components).
         Wait, the rule is: if we pick two cycles, we can't pick any nodes that 
         would require traversing an edge twice. In a functional graph, 
         if we pick two cycles from different components, we can't connect them.
         The actual optimal strategy:
         1. Find all cycles.
         2. Find the maximum cycle size.
         3. Find the maximum path length that ends in a cycle (this is just the cycle size 
            if we consider the cycle itself).
         4. The answer is max(max_cycle_size, max_path_length_ending_in_cycle + second_max_cycle_size_from_different_component).
         Actually, the simplest way:
         A component has one cycle. Let cycle size be C and max path length leading to cycle be P.
         The total nodes we can get from one component is C + P (where P is the longest path 
         ending at a cycle node, not including the cycle nodes).
         Wait, if we pick a cycle and a path, we can't pick another cycle.
         If we pick two cycles, they must be from different components.
         Correct logic:
         - For each component:
           - Find the cycle size.
           - Find the longest path that ends at a cycle node.
         - Result is max(
             max(cycle_size + path_to_cycle), 
             sum of two largest cycle_sizes from different components
           )
         Wait, the "path to cycle" can only be used if we don't pick another cycle.
         If we pick two cycles, we can't pick any paths.
         So:
         1. Find all cycles and their sizes.
         2. Find the max (cycle_size + max_path_to_that_cycle).
         3. Find the sum of the two largest cycle sizes.
         """
    n = len(invitations)
    adj = [0] * n
    in_degree = [0] * n
    for u, v in invitations:
        adj[u] = v
        in_degree[v] += 1

    # Use Kahn's algorithm (topological sort) to find all nodes not in any cycle
    # and to calculate the longest path ending at each node.
    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    # max_path[i] is the length of the longest path ending at node i
    max_path = [0] * n
    visited = [False] * n
    
    idx = 0
    while idx < len(queue):
        u = queue[idx]
        idx += 1
        visited[u] = True
        v = adj[u]
        # Update the longest path ending at v
        max_path[v] = max(max_path[v], max_path[u] + 1)
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

    # Now, nodes with in_degree > 0 are part of cycles
    cycle_sizes = []
    max_single_component_total = 0

    for i in range(n):
        if not visited[i] and in_degree[i] > 0:
            # We found a new cycle
            curr = i
            cycle_nodes = []
            while not visited[curr]:
                visited[curr] = True
                cycle_nodes.append(curr)
                curr = adj[curr]
            
            cycle_size = len(cycle_nodes)
            cycle_sizes.append(cycle_size)
            
            # For this specific cycle, find the longest path leading into any of its nodes
            max_p_to_cycle = 0
            for node in cycle_nodes:
                max_p_to_cycle = max(max_p_to_cycle, max_path[node])
            
            # Option 1: One cycle + its longest incoming path
            max_single_component_total = max(max_single_component_total, cycle_size + max_p_to_cycle)

    # Option 2: Two cycles from different components
    # We need the two largest cycle sizes.
    # Note: cycle_sizes contains sizes of cycles from different components.
    # If we pick two cycles, we can't pick any paths.
    two_cycles_total = 0
    if len(cycle_sizes) >= 2:
        # Sort to get the two largest
        sorted_cycles = sorted(cycle_sizes, reverse=True)
        two_cycles_total = sorted_cycles[0] + sorted_cycles[1]
    elif len(cycle_sizes) == 1:
        two_cycles_total = sorted(cycle_sizes, reverse=True)[0]

    return max(max_single_component_total, two_cycles_total)
