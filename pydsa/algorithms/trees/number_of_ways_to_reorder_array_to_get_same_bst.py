METADATA = {
    "id": 1569,
    "name": "Number of Ways to Reorder Array to Get Same BST",
    "slug": "number-of-ways-to-reorder-array-to-get-same-bst",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["recursion", "divide_and_conquer", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to reorder an array such that it results in the same Binary Search Tree structure.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the number of ways to reorder the array to produce the same BST.
    
    The core idea is that for any root, the elements smaller than the root 
    and elements larger than the root must maintain their relative order 
    within their respective subtrees. The total ways is the product of 
    ways to arrange the left subtree, ways to arrange the right subtree, 
    and the number of ways to interleave the two sequences.

    Args:
        arr: A list of unique integers representing the preorder traversal of a BST.

    Returns:
        The number of ways to reorder the array modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7])
        39312
        >>> solve([2, 1, 3])
        1
    """
    MOD = 10**9 + 7
    n = len(arr)

    # Precompute Pascal's triangle for combinations (nCr) to avoid repeated factorial math
    # This allows O(1) lookup for combinations during recursion.
    combinations = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        combinations[i][0] = 1
        for j in range(1, i + 1):
            combinations[i][j] = (combinations[i - 1][j - 1] + combinations[i - 1][j]) % MOD

    def count_ways(elements: list[int]) -> int:
        if len(elements) <= 2:
            return 1

        root = elements[0]
        left_subtree = []
        right_subtree = []

        # Partition the remaining elements into left and right subtrees based on the root
        for i in range(1, len(elements)):
            if elements[i] < root:
                left_subtree.append(elements[i])
            else:
                right_subtree.append(elements[i])

        left_count = len(left_subtree)
        right_count = len(right_subtree)

        # Recursive step: ways = (ways_left * ways_right * combinations(total_slots, left_slots))
        # We use combinations to choose which positions in the sequence the left elements will occupy.
        ways_left = count_ways(left_subtree)
        ways_right = count_ways(right_subtree)
        
        # Interleave the two subtrees using the precomputed combinations table
        interleave_ways = combinations[left_count + right_count][left_count]

        return (ways_left * ways_right * interleave_ways) % MOD

    return count_ways(arr)
