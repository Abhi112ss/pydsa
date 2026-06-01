METADATA = {
    "id": 1156,
    "name": "Swap For Longest Repeated Character Substring",
    "slug": "swap-for-longest-repeated-character-substring",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "string", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring of the same character that can be obtained by performing at most one swap of two characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring of the same character 
    obtainable by at most one swap.

    Args:
        s: The input string.

    Returns:
        The length of the longest possible repeated character substring.

    Examples:
        >>> solve("ABAB")
        4
        >>> solve("AABAA")
        5
        >>> solve("ABAA")
        4
    """
    if not s:
        return 0

    # Pre-calculate the lengths of contiguous blocks of the same character.
    # blocks stores tuples of (character, length_of_block)
    blocks = []
    if s:
        current_char = s[0]
        current_len = 0
        for char in s:
            if char == current_char:
                current_len += 1
            else:
                blocks.append((current_char, current_len))
                current_char = char
                current_len = 1
        blocks.append((current_char, current_len))

    max_len = 0
    # Map to store the total count of each character in the entire string
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Iterate through each contiguous block to see how it can be extended
    for i in range(len(blocks)):
        char, length = blocks[i]
        
        # Base case: the block itself
        current_potential = length
        
        # Check if we can extend the block by swapping a character from elsewhere
        # If the total count of this character is greater than the current block length,
        # we can always bring one more character to either end of this block.
        if char_counts[char] > length:
            current_potential += 1
            
        # Check if we can merge this block with adjacent blocks of the same character
        # This happens if the blocks are separated by exactly one different character.
        # Example: "AA" + "B" + "AAA" -> the "AA" and "AAA" can be joined if we swap 'B'
        
        # Look ahead to see if the next block is a single character of a different type
        # and the block after that is the same character.
        if i + 2 < len(blocks):
            next_char, next_len = blocks[i+1]
            after_next_char, after_next_len = blocks[i+2]
            
            if next_len == 1 and after_next_char == char:
                # We can swap the single character in the middle with a character 
                # from elsewhere (if available) or just use the existing block.
                # If we have more of 'char' available elsewhere, we get length + 1 + after_next_len
                # If we don't, we can only get length + 1 + after_next_len if we swap the 
                # middle character with one of the 'char's from the 'after_next' block.
                # Actually, the rule is: if we swap the middle char with a char from the 
                # 'after_next' block, we get length + 1 + after_next_len.
                # But we must ensure we don't "use" a character we don't have.
                # If char_counts[char] > length + after_next_len, we can definitely 
                # get length + 1 + after_next_len.
                # If char_counts[char] == length + after_next_len, we can still get 
                # length + 1 + after_next_len by swapping the middle char with one 
                # from the 'after_next' block.
                
                # The only constraint is if we have enough 'char' to fill the gap.
                # If we swap the middle char with a 'char' from the 'after_next' block,
                # the 'after_next' block becomes length-1, but the middle becomes 1.
                # Wait, the logic is simpler: if next_len == 1, we can swap that 
                # single character with a character of the same type from elsewhere.
                # If there are no other characters of that type, we can't.
                # But if we swap the middle char with one from the 'after_next' block,
                # we get: length (current) + 1 (the swapped char) + (after_next_len - 1) (remaining).
                # Total = length + after_next_len.
                # However, if we have a character of the same type elsewhere, 
                # we can get length + 1 + after_next_len.
                
                # Correct logic for merging:
                # If next_len == 1, we can potentially merge blocks[i] and blocks[i+2]
                # if we swap the middle character with a character of type 'char' 
                # from elsewhere.
                # If char_counts[char] > length + after_next_len, we can get length + 1 + after_next_len.
                # If char_counts[char] == length + after_next_len, we can get length + after_next_len.
                # Wait, if char_counts[char] == length + after_next_len, we can swap the 
                # middle char with one from the after_next block, resulting in 
                # length + 1 + (after_next_len - 1) = length + after_next_len.
                
                # Let's refine:
                # If we swap the middle char with a char from elsewhere: length + 1 + after_next_len
                # (Only if char_counts[char] > length + after_next_len)
                # If we swap the middle char with a char from the after_next block: length + after_next_len
                # (Only if char_counts[char] == length + after_next_len)
                
                if char_counts[char] > length + after_next_len:
                    current_potential = max(current_potential, length + 1 + after_next_len)
                elif char_counts[char] == length + after_next_len:
                    current_potential = max(current_potential, length + after_next_len)
                else:
                    # This case shouldn't happen if char_counts is correct
                    current_potential = max(current_potential, length + after_next_len)

        # Also check the previous block for the same pattern (handled by iteration)
        max_len = max(max_len, current_potential)

    # Final check for the case where we just have one block and can add one char
    # This is already covered by the 'char_counts[char] > length' logic.
    
    return max_len
