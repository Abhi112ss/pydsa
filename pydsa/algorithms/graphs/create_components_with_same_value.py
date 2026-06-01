METADATA = {
    "id": 2440,
    "name": "Create Components With Same Value",
    "slug": "create-components-with-same-value",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n * divisors(total_sum))",
    "space_complexity": "O(n)",
    "description": "Partition a tree into the maximum number of components such that each component has the same sum.",
}

def solve(edges: list[list[int]], nums: list[int]) -> int:
    """
    Args:
        edges: A list of undirected edges representing the tree.
        nums: A list of integers where nums[i] is the value of node i.

    Returns:
        The maximum number of components that can be formed with the same sum.
    """
    n = len(nums)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_sum = sum(nums)

    def get_divisors(n: int) -> list[int]:
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i*i != n:
                    divisors.append(n // i)
        return divisors

    def count_components(target_sum: int) -> int:
        count = 0
        
        def dfs(node: int, parent: int) -> int:
            nonlocal count
            current_subtree_sum = nums[node]
            for neighbor in adj[node]:
                if neighbor != parent:
                    current_subtree_sum += dfs(neighbor, node)
            
            if current_subtree_sum == target_sum:
                count += 1
                return 0
            return current_subtree_sum

        final_sum = dfs(0, -1)
        if final_sum == 0:
            return count
        return 0

    max_components = 1
    divisors = get_divisors(total_sum)
    
    for target in divisors:
        if target == total_sum:
            continue
        
        current_count = count_components(target)
        if current_count > 0:
            max_components = max(max_components, current_count)

    return max_components