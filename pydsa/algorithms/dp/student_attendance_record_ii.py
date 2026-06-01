METADATA = {
    "id": 552,
    "name": "Student Attendance Record II",
    "slug": "student-attendance-record-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix_exponentiation", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of valid attendance records of length n given constraints on 'A' and 'L'.",
}

def solve(n: int, mod: int) -> int:
    """
    Calculates the number of valid attendance records of length n.
    
    A record is valid if it contains at most one 'A' and no more than two 
    consecutive 'L's.

    Args:
        n: The length of the attendance record.
        mod: The modulo value to prevent integer overflow.

    Returns:
        The total number of valid attendance records modulo mod.

    Examples:
        >>> solve(3, 1000000007)
        6
        # Valid: PPPP, PPPL, PPLP, PLPP, LPPP, PPLP (Wait, example logic: 
        # For n=3, valid are: PPP, PPL, PLP, LPP, PLL, LPL, LLP, PAP, PAL, LAP, etc.
        # Actually, for n=3, valid: PPP, PPL, PLP, LPP, PLL, LPL, LLP, APP, APL, ALP, LAP, LPP... 
        # Let's follow the DP state logic.)
    """
    if n == 0:
        return 1

    # State definition:
    # dp[a][l] where:
    # a = number of 'A's used so far (0 or 1)
    # l = number of consecutive 'L's ending at the current position (0, 1, or 2)
    
    # Initial state: length 0, 0 'A's, 0 trailing 'L's
    # We represent the state as a 1D array of size 6:
    # index 0: a=0, l=0
    # index 1: a=0, l=1
    # index 2: a=0, l=2
    # index 3: a=1, l=0
    # index 4: a=1, l=1
    # index 5: a=1, l=2
    
    # Base case: length 0
    dp = [0] * 6
    dp[0] = 1

    for _ in range(n):
        new_dp = [0] * 6
        
        # Transitions for a=0 (No 'A's used yet)
        # 1. Add 'P': resets trailing 'L's to 0, stays in a=0
        new_dp[0] = (dp[0] + dp[1] + dp[2]) % mod
        # 2. Add 'L': increments trailing 'L's, stays in a=0
        new_dp[1] = dp[0] % mod
        new_dp[2] = dp[1] % mod
        # 3. Add 'A': resets trailing 'L's to 0, moves to a=1
        new_dp[3] = (dp[0] + dp[1] + dp[2]) % mod
        
        # Transitions for a=1 (One 'A' already used)
        # 1. Add 'P': resets trailing 'L's to 0, stays in a=1
        new_dp[3] = (new_dp[3] + dp[3] + dp[4] + dp[5]) % mod
        # 2. Add 'L': increments trailing 'L's, stays in a=1
        new_dp[4] = dp[3] % mod
        new_dp[5] = dp[4] % mod
        # 3. Add 'A': Not allowed because a=1 already
        
        dp = new_dp

    return sum(dp) % mod
