METADATA = {
    "id": 854,
    "name": "K-Similar Strings",
    "slug": "k-similar-strings",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "string_manipulation", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(N * N!)",
    "space_complexity": "O(N!)",
    "description": "Find the minimum number of swaps required to make two strings identical.",
}

from collections import deque

def solve(s1: str, s2: str) -> int:
    """
    Finds the minimum number of swaps to make s1 equal to s2 using BFS.

    The algorithm treats each string configuration as a node in a graph.
    We use Breadth-First Search to find the shortest path from s1 to s2.
    To optimize the branching factor, we only swap the first character 
    where s1[i] != s2[i] with a valid candidate index j where s1[j] == s2[i].

    Args:
        s1: The starting string.
        s2: The target string.

    Returns:
        The minimum number of swaps required.

    Examples:
        >>> solve("pair", "pira")
        1
        >>> solve("ab", "ba")
        1
    """
    if s1 == s2:
        return 0

    target = s2
    queue = deque([(s1, 0)])
    visited = {s1}
    n = len(s1)

    while queue:
        current_str, distance = queue.popleft()

        # Find the first index where current_str and target differ
        # This significantly reduces the branching factor compared to all possible swaps
        first_mismatch = -1
        for i in range(n):
            if current_str[i] != target[i]:
                first_mismatch = i
                break
        
        if first_mismatch == -1:
            return distance

        # Try swapping current_str[first_mismatch] with all possible indices j > first_mismatch
        # such that current_str[j] == target[first_mismatch]
        for j in range(first_mismatch + 1, n):
            if current_str[j] == target[first_mismatch] and current_str[j] != target[j]:
                # Perform the swap
                chars = list(current_str)
                chars[first_mismatch], chars[j] = chars[j], chars[first_mismatch]
                next_str = "".join(chars)

                if next_str == target:
                    return distance + 1

                if next_str not in visited:
                    visited.add(next_str)
                    queue.append((next_str, distance + 1))

    return -1
