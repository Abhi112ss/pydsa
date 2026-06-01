METADATA = {
    "id": 2092,
    "name": "Find All People With Secret",
    "slug": "find-all-people-with-secret",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "bfs", "union_find"],
    "difficulty": "hard",
    "time_complexity": "O(T * (N log N + E))",
    "space_complexity": "O(N + E)",
    "description": "Determine all people who eventually learn a secret based on meetings occurring at specific times.",
}

def solve(people_count: int, meetings: list[list[int]]) -> list[int]:
    """
    Finds all people who eventually learn a secret based on meeting schedules.

    Args:
        people_count: The total number of people (labeled 0 to people_count - 1).
        meetings: A list of meetings where each meeting is [ti, x, y] 
                  representing time ti, and people x and y meeting.

    Returns:
        A sorted list of integers representing the IDs of people who know the secret.

    Examples:
        >>> solve(4, [[1, 0, 1], [1, 1, 2], [2, 0, 2]])
        [0, 1, 2]
        >>> solve(4, [[1, 0, 1], [1, 2, 3], [2, 1, 2]])
        [0, 1, 2]
    """
    # Sort meetings by time to process them chronologically
    meetings.sort()
    
    # Initially, only person 0 knows the secret
    knows_secret = {0}
    
    # Group meetings by time
    from collections import defaultdict
    time_to_meetings = defaultdict(list)
    for time, person_a, person_b in meetings:
        time_to_meetings[time].append((person_a, person_b))
    
    # Get unique sorted time points
    unique_times = sorted(time_to_meetings.keys())

    for current_time in unique_times:
        current_meetings = time_to_meetings[current_time]
        
        # Build an adjacency list for people meeting at this specific time
        adj = defaultdict(list)
        people_involved = set()
        for u, v in current_meetings:
            adj[u].append(v)
            adj[v].append(u)
            people_involved.add(u)
            people_involved.add(v)
            
        # Find people who already know the secret and can spread it
        # We use BFS/DFS to propagate the secret among people meeting at this time
        newly_infected = []
        visited = set()
        
        # Start BFS from everyone in this time slot who already knows the secret
        queue = []
        for person in people_involved:
            if person in knows_secret:
                queue.append(person)
                visited.add(person)
        
        # Standard BFS to find all reachable people in the current time-slice graph
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            newly_infected.append(u)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        
        # Update the global set of people who know the secret
        for person in queue:
            knows_secret.add(person)

    return sorted(list(knows_secret))
