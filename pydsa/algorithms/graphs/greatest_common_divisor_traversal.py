METADATA = {
    "id": 2709,
    "name": "Greatest Common Divisor Traversal",
    "slug": "greatest-common-divisor-traversal",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "math", "union_find"],
    "difficulty": "hard",
    "time_complexity": "O(N log log N)",
    "space_complexity": "O(N)",
    "description": "Find the size of the largest connected component where edges exist between numbers sharing a common divisor greater than 1.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.max_size = 1 if n > 0 else 0

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            self.max_size = max(self.max_size, self.size[root_i])

def solve(nums: list[int]) -> int:
    """
    Finds the size of the largest connected component in a graph where an edge 
    exists between two numbers if they share a common divisor > 1.

    Args:
        nums: A list of integers.

    Returns:
        The size of the largest connected component.

    Examples:
        >>> solve([2, 3, 4, 6])
        4
        >>> solve([1, 2, 3, 5])
        1
    """
    if not nums:
        return 0

    max_val = max(nums)
    # dsu_nodes maps a number to its index in the nums array.
    # We use a DSU on the indices of the nums array.
    dsu = UnionFind(len(nums))
    
    # prime_to_index stores the index of the first number encountered 
    # that is divisible by a specific prime factor.
    prime_to_index: dict[int, int] = {}

    # Precompute smallest prime factor (SPF) using a sieve for efficient factorization
    spf = list(range(max_val + 1))
    for i in range(2, int(max_val**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_val + 1, i):
                if spf[j] == j:
                    spf[j] = i

    for idx, val in enumerate(nums):
        if val == 1:
            continue
            
        # Factorize the current number using the SPF array
        temp = val
        while temp > 1:
            p = spf[temp]
            
            # If we have seen this prime factor before, union the current 
            # index with the index that first introduced this prime.
            if p in prime_to_index:
                dsu.union(idx, prime_to_index[p])
            else:
                prime_to_index[p] = idx
            
            # Remove all instances of this prime factor
            while temp % p == 0:
                temp //= p

    # If all numbers are 1 or no unions occurred, the max component size is 1
    # unless the input was empty (handled above).
    # However, if nums contains 1s, they are isolated nodes.
    # The DSU max_size tracks the largest component of numbers > 1.
    # If all numbers are 1, max_size will be 1.
    
    # Special case: if all numbers are 1, the loop above never calls union.
    # The DSU size is initialized to 1, which is correct.
    return dsu.max_size
