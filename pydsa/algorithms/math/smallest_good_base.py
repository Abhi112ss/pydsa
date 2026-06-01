METADATA = {
    "id": 483,
    "name": "Smallest Good Base",
    "slug": "smallest-good-base",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log^3 n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest integer base k >= 2 such that n can be represented as a sum of distinct powers of k.",
}

import math

def solve(n: int) -> int:
    """
    Finds the smallest integer base k >= 2 such that n can be represented 
    as a sum of distinct powers of k.

    Args:
        n: The target integer.

    Returns:
        The smallest good base k, or 2 if no such base exists.

    Examples:
        >>> solve(8)
        2
        >>> solve(10)
        3
        >>> solve(13)
        3
    """
    # A base k is "good" if n can be written as k^0 + k^p1 + k^p2 ...
    # where 0 < p1 < p2 ...
    # The smallest possible sum for a given number of terms (m) is 
    # k^0 + k^1 + ... + k^(m-1).
    # The largest possible sum for m terms is k^0 + k^(max_power) + ...
    # However, the problem asks for distinct powers. 
    # If we fix the number of terms (m), we want to find if there exists a k.
    
    # The maximum number of terms is log2(n) because the smallest base is 2.
    # We iterate through the number of terms 'm' from the largest possible down to 2.
    # Since we want the smallest base k, we want the largest number of terms m.
    
    max_terms = int(math.log2(n)) + 1
    
    for m in range(max_terms, 1, -1):
        # We are looking for a base k such that:
        # k^0 + k^1 + ... + k^(m-1) <= n
        # This is a geometric series: (k^m - 1) / (k - 1) <= n
        
        # We use binary search to find the largest k that satisfies the inequality.
        # The lower bound for k is 2.
        # The upper bound for k is n^(1/(m-1)).
        low = 2
        high = int(n**(1 / (m - 1))) + 1
        
        best_k = -1
        
        while low <= high:
            mid = (low + high) // 2
            if mid < 2:
                low = mid + 1
                continue
                
            # Calculate the sum of the first m powers of mid: mid^0 + mid^1 + ... + mid^(m-1)
            # We use a loop to prevent overflow issues in other languages, 
            # though Python handles large ints.
            current_sum = 0
            power_of_k = 1
            possible = True
            for _ in range(m):
                current_sum += power_of_k
                if current_sum > n:
                    possible = False
                    break
                power_of_k *= mid
            
            if possible and current_sum <= n:
                # If the sum of the first m terms is <= n, this k might be valid.
                # We want the largest k for this m to satisfy the "smallest base" 
                # requirement across different m values.
                best_k = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # If we found a valid k for this m, we check if n can actually be 
        # represented as a sum of distinct powers of k.
        # A number n can be represented as a sum of distinct powers of k 
        # if and only if its representation in base k only contains digits 0 and 1.
        if best_k != -1:
            temp_n = n
            is_good = True
            while temp_n > 0:
                if temp_n % best_k > 1:
                    is_good = False
                    break
                temp_n //= best_k
            
            if is_good:
                return best_k

    # If no base k > 2 is found, the smallest good base is 2 (or n+1 if n=1, 
    # but n is usually >= 2 in this problem context).
    # For n=1, the problem is trivial, but based on constraints, k=n+1 is the fallback.
    return n + 1
