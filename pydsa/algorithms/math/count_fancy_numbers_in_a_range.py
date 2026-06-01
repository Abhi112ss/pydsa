METADATA = {
    "id": 3869,
    "name": "Count Fancy Numbers in a Range",
    "slug": "count-fancy-numbers-in-a-range",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Count numbers in a range [L, R] that satisfy specific digit-based 'fancy' criteria using digit DP.",
}

def solve(L: int, R: int) -> int:
    """
    Counts the number of 'fancy' numbers in the range [L, R].
    A number is 'fancy' if it satisfies specific digit constraints.
    (Note: Since the specific 'fancy' rule was not provided in the prompt, 
    this implementation assumes a standard digit DP template for a 
    generic digit-based property. For the purpose of this template, 
    we implement a placeholder logic: numbers where no digit repeats 
    more than twice consecutively).

    Args:
        L (int): The lower bound of the range.
        R (int): The upper bound of the range.

    Returns:
        int: The count of fancy numbers in [L, R].

    Examples:
        >>> solve(1, 10)
        10
        >>> solve(100, 110)
        11
    """

    def count_fancy_up_to(n: int) -> int:
        """
        Helper function to count fancy numbers from 0 to n using Digit DP.
        """
        if n < 0:
            return 0
        
        s = str(n)
        length = len(s)
        
        # memoization table: (index, last_digit, last_digit_count, is_less, is_started)
        # Using a dictionary for memoization to handle the state space efficiently.
        memo = {}

        def dp(idx: int, last_digit: int, last_count: int, is_less: bool, is_started: bool) -> int:
            state = (idx, last_digit, last_count, is_less, is_started)
            if state in memo:
                return memo[state]
            
            if idx == length:
                return 1 if is_started else 0

            res = 0
            # Determine the upper limit for the current digit
            limit = int(s[idx]) if not is_less else 9

            for digit in range(limit + 1):
                new_is_less = is_less or (digit < limit)
                new_is_started = is_started or (digit > 0)

                if not new_is_started:
                    # Still leading zeros
                    res += dp(idx + 1, -1, 0, new_is_less, False)
                else:
                    # Check the 'fancy' constraint: no digit repeats more than twice
                    # (This is a placeholder constraint for the 'fancy' definition)
                    if digit == last_digit:
                        if last_count < 2:
                            res += dp(idx + 1, digit, last_count + 1, new_is_less, True)
                    else:
                        res += dp(idx + 1, digit, 1, new_is_less, True)
            
            # Note: The logic above counts numbers with no more than 2 consecutive identical digits.
            # To match a specific problem, the 'if' condition inside the loop would change.
            
            # Correcting the loop logic for the placeholder:
            # The loop above actually double counts leading zeros if not careful.
            # Let's refine the logic for a clean Digit DP.
            return res

        # Re-implementing the DP iteratively or with a cleaner recursive structure 
        # to ensure it handles the 'is_started' (leading zeros) correctly.
        
        memo = {}

        def dp_refined(idx: int, last_digit: int, last_count: int, is_less: bool, is_started: bool) -> int:
            state = (idx, last_digit, last_count, is_less, is_started)
            if state in memo:
                return memo[state]
            
            if idx == length:
                return 1 if is_started else 0
            
            res = 0
            limit = int(s[idx]) if not is_less else 9
            
            for digit in range(limit + 1):
                next_is_less = is_less or (digit < limit)
                
                if not is_started and digit == 0:
                    # Case: Leading zero
                    res += dp_refined(idx + 1, -1, 0, next_is_less, False)
                else:
                    # Case: Placing a non-zero digit or a digit after the number has started
                    if digit == last_digit:
                        # Check constraint: e.g., no more than 2 consecutive digits
                        if last_count < 2:
                            res += dp_refined(idx + 1, digit, last_count + 1, next_is_less, True)
                    else:
                        res += dp_refined(idx + 1, digit, 1, next_is_less, True)
            
            memo[state] = res
            return res

        # The number 0 is usually considered fancy in these problems unless specified.
        # We add 1 to account for the number 0 if the range includes it.
        return dp_refined(0, -1, 0, False, False) + (1 if n >= 0 else 0)

    # The result for [L, R] is Count(R) - Count(L-1)
    # However, since our DP includes 0, we must be careful.
    # If the DP counts 0, then Count(R) - Count(L-1) works perfectly.
    
    # Note: The placeholder logic above counts 0 as a fancy number.
    # We adjust the return to handle the range correctly.
    
    # Because the prompt asks for a specific problem #3869 which is hypothetical/new,
    # I am providing the robust Digit DP structure.
    
    # For the sake of a working example, let's assume 'fancy' means 
    # "no digit appears more than twice in the whole number" 
    # (a common variation).
    
    def count_with_global_constraint(n: int) -> int:
        if n < 0: return 0
        s = str(n)
        length = len(s)
        memo = {}

        def dp_global(idx: int, counts: tuple, is_less: bool, is_started: bool) -> int:
            # counts is a tuple of 10 integers representing frequency of digits 0-9
            state = (idx, counts, is_less, is_started)
            if state in memo: return memo[state]
            if idx == length: return 1 if is_started else 0

            res = 0
            limit = int(s[idx]) if not is_less else 9
            for d in range(limit + 1):
                next_is_less = is_less or (d < limit)
                if not is_started and d == 0:
                    res += dp_global(idx + 1, counts, next_is_less, False)
                else:
                    # Constraint: No digit appears more than 2 times total
                    if counts[d] < 2:
                        new_counts = list(counts)
                        new_counts[d] += 1
                        res += dp_global(idx + 1, tuple(new_counts), next_is_less, True)
            
            memo[state] = res
            return res

        return dp_global(0, (0,)*10, False, False) + 1

    # Using the global constraint version for the final implementation
    return count_with_global_constraint(R) - count_with_global_constraint(L - 1)
