METADATA = {
    "id": 1923,
    "name": "Longest Common Subpath",
    "slug": "longest-common-subpath",
    "category": "Hard",
    "aliases": [],
    "tags": ["binary_search", "rolling_hash", "string_matching"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest common subpath present in all given arrays using binary search and rolling hash.",
}

def solve(nums1: list[int], nums2: list[int], nums3: list[int]) -> int:
    """
    Finds the length of the longest common subpath present in all three arrays.

    Args:
        nums1: The first array of integers.
        nums2: The second array of integers.
        nums3: The third array of integers.

    Returns:
        The length of the longest common subpath.

    Examples:
        >>> solve([1,2,3,2,1], [3,2,1,4,7], [1,2,3,4,1])
        3
        >>> solve([1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5])
        5
    """
    # Use two large primes for double hashing to minimize collision probability
    # MOD1 and MOD2 are large primes, BASE is a prime larger than any possible element
    # However, since elements can be up to 10^9, we use a large prime base and 
    # handle collisions by using a large enough modulus or double hashing.
    # For LeetCode constraints, a single 64-bit prime or double 32-bit hashing is common.
    MOD = (1 << 61) - 1  # Mersenne prime for efficient modulo and low collision
    BASE = 1000000007

    def check(length: int) -> bool:
        """Checks if there is a common subpath of the given length."""
        if length == 0:
            return True

        # Precompute BASE^length % MOD
        power = pow(BASE, length, MOD)

        def get_hashes(arr: list[int]) -> set[int]:
            """Computes all rolling hashes of a specific length for an array."""
            hashes = set()
            current_hash = 0
            
            # Initial window hash
            for i in range(length):
                current_hash = (current_hash * BASE + arr[i]) % MOD
            hashes.add(current_hash)

            # Rolling the window
            for i in range(length, len(arr)):
                # Remove leading element and add trailing element
                current_hash = (current_hash * BASE + arr[i] - arr[i - length] * power) % MOD
                hashes.add(current_hash)
            return hashes

        # Get hashes from the first array
        common_hashes = get_hashes(nums1)
        
        # Intersect with hashes from the second array
        if not common_hashes:
            return False
        
        # We must manually intersect to avoid creating massive sets if not needed
        # but for simplicity in Python, set intersection is highly optimized.
        current_hashes_2 = get_hashes(nums2)
        common_hashes &= current_hashes_2
        
        if not common_hashes:
            return False

        # Intersect with hashes from the third array
        current_hashes_3 = get_hashes(nums3)
        common_hashes &= current_hashes_3
        
        return len(common_hashes) > 0

    # Binary search on the possible length of the subpath
    low = 1
    high = min(len(nums1), len(nums2), len(nums3))
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
