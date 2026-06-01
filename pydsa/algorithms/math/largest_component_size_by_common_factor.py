METADATA = {
    "id": 952,
    "name": "Largest Component Size by Common Factor",
    "slug": "largest-component-size-by-common-factor",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "prime_factorization", "math"],
    "difficulty": "hard",
    "time_complexity": "O(N * sqrt(max(nums)))",
    "space_complexity": "O(max(nums))",
    "description": "Find the size of the largest component in a graph where an edge exists between two numbers if they share a common factor greater than 1.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.num_sets = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.num_sets -= 1
            return True
        return False

def solve(nums: list[int]) -> int:
    """
    Finds the size of the largest component in a graph where nodes are connected 
    if they share a common factor > 1.

    Args:
        nums: A list of integers.

    Returns:
        The size of the largest connected component.

    Examples:
        >>> solve([2, 5, 6, 9, 15])
        5
        >>> solve([4, 6, 15, 35])
        3
    """
    if not nums:
        return 0

    max_val = max(nums)
    dsu = UnionFind(max_val)

    # Instead of comparing all pairs (O(N^2)), we iterate through each number
    # and union the number with its prime factors.
    for num in nums:
        temp = num
        divisor = 2
        # Standard prime factorization approach
        while divisor * divisor <= temp:
            if temp % divisor == 0:
                # Union the number with its prime factor
                dsu.union(num, divisor)
                while temp % divisor == 0:
                    temp //= divisor
            divisor += 1
        
        # If temp > 1, the remaining temp is a prime factor
        if temp > 1:
            dsu.union(num, temp)

    # Count the size of each component formed by the numbers in the input list
    component_sizes = {}
    for num in nums:
        root = dsu.find(num)
        component_sizes[root] = component_sizes.get(root, 0) + 1

    return max(component_sizes.values()) if component_sizes else 0
