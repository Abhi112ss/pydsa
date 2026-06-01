METADATA = {
    "id": 1666,
    "name": "Change the Root of a Binary Tree",
    "slug": "change_the_root_of_a_binary_tree",
    "category": "tree",
    "aliases": [],
    "tags": ["dfs", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Compute sum of distances from each queried node to all other nodes after re-rooting the tree.",
}


def solve() -> None:
    """Read a tree and queries, output sum of distances for each query node.

    Input format:
        n
        u1 v1
        u2 v2
        ...
        u_{n-1} v_{n-1}
        q
        query1 query2 ... query_q

    Args:
        None (reads from standard input).

    Returns:
        None (writes space‑separated answers to standard output).

    Example:
        Input:
            6
            0 1
            0 2
            2 3
            2 4
            2 5
            3
            0 2 5
        Output:
            15 13 15
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        adjacency[u].append(v)
        adjacency[v].append(u)

    q = int(next(it))
    queries = [int(next(it)) for _ in range(q)]

    # First DFS: compute subtree sizes and total distance from node 0.
    subtree_size: list[int] = [0] * n
    total_distance = 0

    sys.setrecursionlimit(10 ** 6)

    def dfs1(node: int, parent: int, depth: int) -> None:
        nonlocal total_distance
        total_distance += depth  # accumulate distance from root to this node
        subtree_size[node] = 1
        for neighbor in adjacency[node]:
            if neighbor == parent:
                continue
            dfs1(neighbor, node, depth + 1)
            subtree_size[node] += subtree_size[neighbor]

    dfs1(0, -1, 0)

    # answer[node] will hold sum of distances from node to all others.
    answer: list[int] = [0] * n
    answer[0] = total_distance

    # Second DFS: reroot using the formula answer[child] = answer[parent] + (n - 2*size_child)
    def dfs2(node: int, parent: int) -> None:
        for neighbor in adjacency[node]:
            if neighbor == parent:
                continue
            answer[neighbor] = answer[node] + (n - 2 * subtree_size[neighbor])
            dfs2(neighbor, node)

    dfs2(0, -1)

    output = " ".join(str(answer[q_node]) for q_node in queries)
    sys.stdout.write(output)