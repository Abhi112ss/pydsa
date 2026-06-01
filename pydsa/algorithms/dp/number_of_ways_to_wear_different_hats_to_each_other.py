METADATA = {
    "id": 1434,
    "name": "Number of Ways to Wear Different Hats to Each Other",
    "slug": "number-of-ways-to-wear-different-hats-to-each-other",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * 2^m)",
    "space_complexity": "O(2^m)",
    "description": "Find the number of ways to assign unique hats to people such that each person wears a hat they like.",
}

def solve(people_likes: list[list[int]], num_hats: int) -> int:
    """
    Calculates the number of ways to assign unique hats to people.

    Args:
        people_likes: A list of lists where people_likes[i] contains the 
            hat indices (1-indexed) that person i likes.
        num_hats: The total number of available hats.

    Returns:
        The number of ways to assign hats modulo 10^9 + 7.

    Examples:
        >>> solve([[0,1],[1,2],[0,2]], 3)
        1
        >>> solve([[0],[1],[2]], 3)
        1
    """
    MOD = 1_000_000_007
    num_people = len(people_likes)
    
    # Since the number of hats (m) is small (up to 10), we use a bitmask 
    # to represent the set of hats already used.
    # dp[mask] = number of ways to assign hats represented by the mask 
    # to the first 'k' people.
    dp = [0] * (1 << num_hats)
    dp[0] = 1

    # We iterate person by person. For each person, we try to assign 
    # one of their liked hats that hasn't been used yet.
    for person_idx in range(num_people):
        # We must iterate backwards through the masks to ensure we are 
        # building upon the results of the previous person (preventing 
        # using the same person multiple times for the same mask).
        new_dp = [0] * (1 << num_hats)
        
        # Optimization: Instead of iterating all masks, we only care about
        # masks that were reachable by the previous person.
        for mask in range(1 << num_hats):
            if dp[mask] == 0:
                continue
            
            # Try every hat the current person likes
            for hat_id in people_likes[person_idx]:
                # Convert 0-indexed hat_id to bit position
                # Note: The problem uses 0-indexed in the input list 
                # but the logic remains consistent.
                hat_bit = 1 << hat_id
                
                # If the hat is not already in the mask
                if not (mask & hat_bit):
                    new_mask = mask | hat_bit
                    new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD
        
        # If a person cannot wear any hat, the total ways will eventually be 0.
        # We update dp to the state after this person.
        dp = new_dp

    # The answer is the sum of all ways to have assigned hats to all people.
    # Since we processed exactly 'num_people' iterations, any non-zero 
    # entry in dp represents a valid assignment of 'num_people' hats.
    return sum(dp) % MOD
