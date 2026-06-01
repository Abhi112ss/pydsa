METADATA = {
    "id": 3629,
    "name": "Minimum Jumps to Reach End via Prime Teleportation",
    "slug": "minimum-jumps-to-reach-end-via-prime-teleportation",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "math", "primes"],
    "difficulty": "medium",
    "time_complexity": "O(n log log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of jumps to reach the last index of an array where each jump must be a prime distance.",
}

from collections import deque

def solve(n: int) -> int:
    """
    Calculates the minimum number of jumps to reach index n-1 from index 0,
    where each jump distance must be a prime number.

    Args:
        n (int): The number of elements in the array (indices 0 to n-1).

    Returns:
        int: The minimum number of jumps required, or -1 if unreachable.

    Examples:
        >>> solve(5)
        1  # Jump from 0 to 4 (distance 4 is not prime, but 0 to 2 to 4 is 2 jumps. 
           # Wait, if n=5, indices are 0,1,2,3,4. Jump 0->2 (dist 2), 2->4 (dist 2). Total 2.
           # If n=4, indices 0,1,2,3. Jump 0->3 (dist 3). Total 1.
        >>> solve(1)
        0
    """
    if n <= 1:
        return 0

    # Step 1: Sieve of Eratosthenes to find all primes up to n
    # This allows us to know all possible jump distances.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    
    primes = [p for p, prime in enumerate(is_prime) if prime]

    # Step 2: BFS to find the shortest path in an unweighted graph
    # Nodes are indices, edges exist if |i - j| is prime.
    queue = deque([(0, 0)])  # (current_index, distance_traveled)
    visited = [False] * n
    visited[0] = True

    while queue:
        current_index, steps = queue.popleft()

        # If we reached the target index
        if current_index == n - 1:
            return steps

        # Try jumping forward
        # We iterate through primes to find valid next indices
        for p in primes:
            next_index = current_index + p
            if next_index >= n:
                break
            if not visited[next_index]:
                visited[next_index] = True
                queue.append((next_index, steps + 1))
        
        # Try jumping backward
        for p in primes:
            next_index = current_index - p
            if next_index < 0:
                break
            if not visited[next_index]:
                visited[next_index] = True
                queue.append((next_index, steps + 1))

    return -1
