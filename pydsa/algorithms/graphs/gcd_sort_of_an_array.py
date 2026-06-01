METADATA = {
    "id": 1998,
    "name": "GCD Sort of an Array",
    "slug": "gcd-sort-of-an-array",
    "category": "Hard",
    "aliases": [],
    "tags": ["union_find", "math", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(N log N + MAX_VAL log log MAX_VAL)",
    "space_complexity": "O(N + MAX_VAL)",
    "description": "Determine if an array can be sorted by swapping elements that have a GCD greater than 1.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

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
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

def solve(nums: list[int]) -> bool:
    """
    Determines if the array can be sorted by swapping elements with GCD > 1.
    
    The core idea is that if two numbers share a prime factor, they belong to the 
    same connected component in a graph where edges exist between numbers with GCD > 1.
    Any elements within the same component can be permuted arbitrarily.

    Args:
        nums: A list of integers.

    Returns:
        True if the array can be sorted, False otherwise.

    Examples:
        >>> solve([2, 1, 3, 1, 2])
        False
        >>> solve([10, 5, 9, 3])
        True
    """
    if not nums:
        return True

    max_val = max(nums)
    dsu = UnionFind(max_val + 1)

    # Sieve-like approach to union numbers with their prime factors.
    # Instead of checking all pairs (O(N^2)), we connect each number to its prime factors.
    # This ensures that if gcd(a, b) > 1, a and b will end up in the same component.
    visited_primes = [False] * (max_val + 1)
    for i in range(2, max_val + 1):
        if not visited_primes[i]:
            # i is a prime number
            for multiple in range(i, max_val + 1, i):
                visited_primes[multiple] = True
                # We don't know if 'multiple' is in 'nums' yet, but we union 
                # the value 'multiple' with its prime factor 'i'.
                # This builds the connectivity structure for all possible values.
                dsu.union(i, multiple)

    # We need to check if the elements in their current positions can reach 
    # their target positions in the sorted array.
    sorted_nums = sorted(nums)
    
    for original, target in zip(nums, sorted_nums):
        if original == target:
            continue
        
        # If the values are different, they must belong to the same connected component
        # to be swappable via a sequence of GCD > 1 swaps.
        if dsu.find(original) != dsu.find(target):
            return False

    return True
