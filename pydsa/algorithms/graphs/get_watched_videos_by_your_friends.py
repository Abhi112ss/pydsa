METADATA = {
    "id": 1311,
    "name": "Get Watched Videos by Your Friends",
    "slug": "get-watched-videos-by-your-friends",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "hash_map", "sorting", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(V + E + K log K)",
    "space_complexity": "O(V)",
    "description": "Find all videos watched by friends at a specific distance from a user, sorted by frequency and lexicographical order.",
}

from collections import deque, defaultdict

def solve(n: int, edges: list[list[int]], videos: list[list[int]], user: int, level: int) -> list[str]:
    """
    Finds videos watched by friends at a specific distance 'level' from the user.

    Args:
        n: The number of users.
        edges: A list of undirected edges representing friendships.
        videos: A list of lists where videos[i] contains video IDs watched by user i.
        user: The ID of the starting user.
        level: The distance from the user to find friends.

    Returns:
        A list of video IDs (as strings) sorted by frequency (descending) 
        and then lexicographically (ascending).

    Examples:
        >>> solve(4, [[0,1],[1,2],[2,3]], [[10,20],[20,30],[30,40],[40,50]], 0, 2)
        ['30', '40']
    """
    # Build adjacency list for the graph
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # BFS to find all users at exactly 'level' distance
    visited = {user}
    queue = deque([(user, 0)])
    target_friends = []

    while queue:
        curr_user, curr_dist = queue.popleft()

        if curr_dist == level:
            target_friends.append(curr_user)
            # Since BFS processes level by level, once we reach level, 
            # we don't need to explore neighbors of these nodes for this specific problem.
            continue
        
        if curr_dist < level:
            for neighbor in adj[curr_user]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, curr_dist + 1))

    # Count frequencies of videos watched by the target friends
    video_counts = defaultdict(int)
    for friend in target_friends:
        for video_id in videos[friend]:
            video_counts[video_id] += 1

    # Sort videos: 
    # 1. By frequency descending (-video_counts[v])
    # 2. By video ID ascending (v)
    # Note: video_id is an integer, but the problem asks for string output.
    # We sort the integer keys first to ensure correct lexicographical behavior 
    # if the problem implies numeric order, but standard LeetCode 1311 
    # expects string representation of the IDs.
    
    sorted_videos = sorted(
        video_counts.keys(), 
        key=lambda v: (-video_counts[v], v)
    )

    return [str(v) for v in sorted_videos]
