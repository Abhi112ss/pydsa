METADATA = {
    "id": 753,
    "name": "Cracking the Safe",
    "slug": "cracking-the-safe",
    "category": "Graph",
    "aliases": [],
    "tags": ["eulerian_path", "graph", "backtracking", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(k^n)",
    "space_complexity": "O(k^n)",
    "description": "Find the shortest string that contains all possible combinations of n characters from an alphabet of size k.",
}

def solve(n: int, k: int) -> str:
    """
    Args:
        n: The length of each combination.
        k: The number of possible characters (0 to k-1).

    Returns:
        The shortest string containing all possible n-length combinations.
    """
    alphabet = [str(i) for i in range(k)]
    visited_edges = set()
    sequence = []

    def build_eulerian_path(current_node: str) -> None:
        for i in range(k):
            next_char = alphabet[i]
            edge = current_node + next_char
            if edge not in visited_edges:
                visited_edges.add(edge)
                next_node = edge[1:]
                build_eulerian_path(next_node)
                sequence.append(next_char)

    start_node = "0" * (n - 1) if n > 1 else ""
    
    if n == 1:
        return "".join(alphabet)

    build_eulerian_path(start_node)
    
    return start_node + "".join(reversed(sequence))

def solve_optimized(n: int, k: int) -> str:
    """
    Args:
        n: The length of each combination.
        k: The number of possible characters (0 to k-1).

    Returns:
        The shortest string containing all possible n-length combinations.
    """
    if n == 1:
        return "".join(str(i) for i in range(k))

    visited = set()
    result = []

    def dfs(node: str) -> None:
        for i in range(k):
            edge = node + str(i)
            if edge not in visited:
                visited.add(edge)
                dfs(edge[1:])
                result.append(str(i))

    start_node = "0" * (n - 1)
    dfs(start_node)
    
    return start_node + "".join(result[::-1])

def solve(n: int, k: int) -> str:
    """
    Args:
        n: The length of each combination.
        k: The number of possible characters (0 to k-1).

    Returns:
        The shortest string containing all possible n-length combinations.
    """
    if n == 1:
        return "".join(str(i) for i in range(k))

    visited = set()
    path = []

    def find_path(current_prefix: str) -> None:
        for i in range(k):
            combination = current_prefix + str(i)
            if combination not in visited:
                visited.add(combination)
                find_path(combination[1:])
                path.append(str(i))

    start_node = "0" * (n - 1)
    find_path(start_node)
    
    return start_node + "".join(path[::-1])