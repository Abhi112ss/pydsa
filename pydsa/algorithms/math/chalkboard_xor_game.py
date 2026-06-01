METADATA = {
    "id": 810,
    "name": "Chalkboard XOR Game",
    "slug": "chalkboard-xor-game",
    "category": "Game Theory",
    "aliases": [],
    "tags": ["game_theory", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if Alice wins a game where players remove elements to manipulate the XOR sum of a chalkboard.",
}

def solve(chalkboard: list[int]) -> bool:
    """
    Determines if Alice wins the Chalkboard XOR Game.

    In this game, Alice and Bob take turns removing an element from the chalkboard.
    Alice wins if the XOR sum of the remaining elements is 0 after her turn.
    The game ends when the chalkboard is empty.

    Args:
        chalkboard: A list of integers representing the numbers on the chalkboard.

    Returns:
        True if Alice wins, False otherwise.

    Examples:
        >>> solve([1, 1, 2, 2])
        True
        >>> solve([1, 2, 3])
        True
        >>> solve([1, 2, 4])
        False
    """
    n = len(chalkboard)
    
    # Calculate the total XOR sum of all elements on the chalkboard.
    total_xor_sum = 0
    for num in chalkboard:
        total_xor_sum ^= num

    # Case 1: If the initial XOR sum is already 0, Alice can win by 
    # picking an element such that the remaining XOR sum is 0.
    # However, the rule is Alice wins if the XOR sum is 0 AFTER her turn.
    # If total_xor_sum is 0, Alice can pick any element 'x'. 
    # The new XOR sum will be 0 ^ x = x. This doesn't immediately help.
    # Let's re-evaluate: Alice wins if she can pick an element 'x' 
    # such that (total_xor_sum ^ x) == 0.
    # This is only possible if total_xor_sum == x.
    # Since x is an element in the array, if total_xor_sum is present in the array,
    # Alice can pick it and leave a 0 XOR sum.
    
    # Actually, the game theory logic for this specific problem:
    # Alice wins if:
    # 1. The total XOR sum is 0. (Wait, if total XOR is 0, any x she picks 
    #    makes the new XOR sum x. If x != 0, she doesn't win immediately.
    #    But if total XOR is 0, and she picks x, the new sum is x. 
    #    If she can pick x such that x is the total XOR sum, she wins.)
    
    # Correct Logic:
    # Alice wins if:
    # 1. The total XOR sum is 0. (Actually, if total XOR is 0, she can't win 
    #    on the first move unless there's a 0 in the array. But the problem 
    #    implies she wins if she can make the XOR sum 0).
    # 2. The number of elements is even. If n is even, Alice can always 
    #    force a win by mirroring Bob's moves or managing the parity.
    
    # Let's refine:
    # If total_xor_sum == 0, Alice wins because she can pick an element 
    # such that the remaining XOR sum is 0? No, if total_xor is 0, 
    # picking x makes it 0 ^ x = x.
    # If total_xor_sum != 0, Alice wins if she can pick x = total_xor_sum.
    # If she picks x = total_xor_sum, the new XOR sum is total_xor_sum ^ total_xor_sum = 0.
    
    # Wait, the standard solution for this specific LeetCode problem:
    # Alice wins if:
    # - The total XOR sum is 0.
    # - OR the number of elements is even.
    
    # Let's re-verify:
    # If n is even, Alice can always win.
    # If n is odd:
    #    If total_xor_sum == 0, Alice wins.
    #    If total_xor_sum != 0, Alice can only win if she can pick x 
    #    such that total_xor_sum ^ x == 0, which means x == total_xor_sum.
    #    But if n is odd and total_xor_sum != 0, can she always win?
    #    Actually, if n is odd and total_xor_sum != 0, Alice can pick x = total_xor_sum 
    #    to make the XOR sum 0. This makes the remaining count (n-1) which is even.
    #    If the count is even and XOR is 0, the next player (Bob) is in a losing position.
    
    # Re-simplifying the logic:
    # Alice wins if:
    # 1. n is even.
    # 2. n is odd AND (total_xor_sum == 0 OR there exists x in chalkboard such that x == total_xor_sum).
    # Actually, if n is odd and total_xor_sum != 0, Alice can pick x = total_xor_sum 
    # to make the XOR sum 0. This is always possible if total_xor_sum is in the array.
    # But wait, if n is odd, and total_xor_sum is NOT in the array, she can't win in one move.
    # However, the problem is simpler:
    # If n is even, Alice wins.
    # If n is odd, Alice wins if total_xor_sum == 0 OR she can pick x = total_xor_sum.
    # But if n is odd, and total_xor_sum is not 0, she can only pick x = total_xor_sum 
    # if such an x exists in the array.
    
    # Let's look at the parity:
    # If n is even, Alice wins.
    # If n is odd, Alice wins if total_xor_sum == 0.
    # Wait, if n is odd and total_xor_sum != 0, Alice can pick x = total_xor_sum 
    # to make the XOR sum 0. This is only possible if total_xor_sum is in the array.
    # But if n is odd, and total_xor_sum is NOT in the array, Alice cannot win on her first move.
    # Does she win later? 
    # If n is even, Alice wins.
    # If n is odd, Alice wins if total_xor_sum == 0.
    # Let's check the constraints and examples.
    # Example 1: [1, 1, 2, 2], n=4 (even) -> True.
    # Example 2: [1, 2, 3], n=3 (odd), XOR = 1^2^3 = 0 -> True.
    # Example 3: [1, 2, 4], n=3 (odd), XOR = 1^2^4 = 7 -> False.
    
    # The logic is:
    # Alice wins if (n % 2 == 0) or (total_xor_sum == 0).
    
    if n % 2 == 0:
        return True
    
    return total_xor_sum == 0
