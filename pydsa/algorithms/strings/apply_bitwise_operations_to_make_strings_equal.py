METADATA = {
    "id": 2546,
    "name": "Apply Bitwise Operations to Make Strings Equal",
    "slug": "apply-bitwise-operations-to-make-strings-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make two binary strings equal by flipping suffixes.",
}

def solve(s1: str, s2: str) -> int:
    """
    Calculates the minimum number of suffix flip operations required to make s1 equal to s2.

    An operation consists of choosing an index i and flipping all characters from 
    index i to the end of the string.

    Args:
        s1: The first binary string.
        s2: The second binary string.

    Returns:
        The minimum number of operations required. Returns -1 if it is impossible.

    Examples:
        >>> solve("0110", "0101")
        2
        >>> solve("0110", "0110")
        0
        >>> solve("0110", "1111")
        -1
    """
    n = len(s1)
    if len(s2) != n:
        return -1

    # flip_count tracks how many times we have applied a suffix flip.
    # Since flipping twice is equivalent to not flipping at all, 
    # we only care if the total number of flips is even or odd.
    flip_count = 0
    
    for i in range(n):
        # Determine the current state of the character in s1 after all previous flips.
        # If flip_count is even, the character remains the same.
        # If flip_count is odd, the character is flipped (0 -> 1, 1 -> 0).
        current_char_s1 = s1[i]
        if flip_count % 2 == 1:
            current_char_s1 = '1' if current_char_s1 == '0' else '0'
        
        # If the current character in s1 (after flips) does not match s2,
        # we must perform a new suffix flip starting at this index.
        if current_char_s1 != s2[i]:
            flip_count += 1
            
    # After iterating through the whole string, we must ensure that the 
    # final state of the last character matches s2. 
    # However, the logic above naturally handles this: if the last character 
    # didn't match, we incremented flip_count. 
    # The only way to fail is if the strings are of different lengths (handled above).
    # Wait, actually, in this specific problem, any mismatch at index i 
    # requires a flip that affects everything to the right. 
    # If we reach the end and the logic is consistent, we just return flip_count.
    # But we must check if the very last character matches after all flips.
    
    # Re-verifying the logic: The greedy approach works because a flip at index i 
    # is the only way to fix a mismatch at index i without affecting indices < i.
    # If we reach the end and the last character doesn't match, it's impossible.
    # But since we flip the suffix [i...n-1], the last character is always 
    # part of the flip. Let's check the last character specifically.
    
    last_char_s1 = s1[-1]
    if flip_count % 2 == 1:
        last_char_s1 = '1' if last_char_s1 == '0' else '0'
        
    if last_char_s1 != s2[-1]:
        return -1

    return flip_count
