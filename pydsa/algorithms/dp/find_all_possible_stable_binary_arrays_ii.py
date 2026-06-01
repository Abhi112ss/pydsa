METADATA = {
    "id": 3130,
    "name": "Find All Possible Stable Binary Arrays II",
    "slug": "find-all-possible-stable-binary-arrays-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "matrix_exponentiation", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of stable binary arrays of length n modulo 10^9 + 7 using matrix exponentiation.",
}

def solve(n: int) -> int:
    """
    Calculates the number of stable binary arrays of length n.
    A binary array is stable if it does not contain the pattern '010' or '101'.
    
    Args:
        n: The length of the binary array.

    Returns:
        The number of stable binary arrays of length n modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        2
        >>> solve(2)
        4
        >>> solve(3)
        6
    """
    MOD = 1_000_000_007

    if n == 1:
        return 2
    if n == 2:
        return 4

    def multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        """Multiplies two 4x4 matrices under modulo."""
        C = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for k in range(4):
                if A[i][k] == 0:
                    continue
                for j in range(4):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    def power(A: list[list[int]], p: int) -> list[list[int]]:
        """Computes A^p using binary exponentiation."""
        res = [[0] * 4 for _ in range(4)]
        for i in range(4):
            res[i][i] = 1
        while p > 0:
            if p % 2 == 1:
                res = multiply(res, A)
            A = multiply(A, A)
            p //= 2
        return res

    # State definition for DP:
    # We track the last two digits to avoid 010 and 101.
    # States: 0: (0,0), 1: (0,1), 2: (1,0), 3: (1,1)
    # Transitions:
    # (0,0) -> (0,0) [add 0], (0,1) [add 1]
    # (0,1) -> (1,1) [add 1] (cannot add 0 because 010 is forbidden)
    # (1,0) -> (0,0) [add 0] (cannot add 1 because 101 is forbidden)
    # (1,1) -> (1,0) [add 0], (1,1) [add 1]
    
    # Transition Matrix T where T[next_state][current_state] = 1
    # State mapping: 0:(0,0), 1:(0,1), 2:(1,0), 3:(1,1)
    # From 0: to 0 (add 0), to 1 (add 1)
    # From 1: to 3 (add 1)
    # From 2: to 0 (add 0)
    # From 3: to 2 (add 0), to 3 (add 1)
    
    # Matrix T:
    # [1, 0, 1, 0]  <- next is (0,0)
    # [1, 0, 0, 0]  <- next is (0,1)
    # [0, 0, 0, 1]  <- next is (1,0)
    # [0, 1, 0, 1]  <- next is (1,1)
    
    T = [
        [1, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1]
    ]

    # Initial vector for n=2:
    # (0,0): 1, (0,1): 1, (1,0): 1, (1,1): 1
    # We need to find T^(n-2) * V_initial
    
    T_n_minus_2 = power(T, n - 2)
    
    # Initial counts for n=2: [1, 1, 1, 1]
    # Result is sum of all elements in T^(n-2) * [1, 1, 1, 1]^T
    # Which is equivalent to summing all elements in the resulting vector.
    
    total_count = 0
    for row in range(4):
        row_sum = 0
        for col in range(4):
            row_sum = (row_sum + T_n_minus_2[row][col]) % MOD
        total_count = (total_count + row_sum) % MOD
        
    # Wait, the logic above sums the vector elements. 
    # Let's calculate the vector V_n = T^(n-2) * V_2
    # V_2 = [1, 1, 1, 1]
    # V_n[i] = sum_{j=0}^3 T_n_minus_2[i][j] * V_2[j]
    # Since V_2 is all 1s, V_n[i] is just the sum of the i-th row of T^(n-2).
    # The total count is sum(V_n[i]) for all i.
    
    # Re-calculating sum of all elements in T^(n-2) is correct because 
    # sum(V_n) = sum_i (sum_j T_ij * 1) = sum_i sum_j T_ij.
    
    # However, the matrix T above is defined such that T[next][curr] = 1.
    # Let's verify:
    # V_n = T * V_{n-1}
    # V_3 = T * [1, 1, 1, 1]^T = [2, 1, 1, 2]^T. Sum = 6. Correct.
    
    final_sum = 0
    for i in range(4):
        for j in range(4):
            final_sum = (final_sum + T_n_minus_2[i][j]) % MOD
            
    return final_sum
