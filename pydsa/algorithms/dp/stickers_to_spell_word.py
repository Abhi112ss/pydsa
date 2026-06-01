METADATA = {
    "id": 691,
    "name": "Stickers to Spell Word",
    "slug": "stickers-to-spell-word",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bitmask", "breadth_first_search"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * m)",
    "space_complexity": "O(2^n)",
    "description": "Find the minimum number of stickers needed to form a target word using bitmask DP.",
}

from collections import deque

def solve(stickers: list[list[str]], target: str) -> int:
    """
    Finds the minimum number of stickers required to form the target word.

    Args:
        stickers: A list of lists, where each sublist contains characters 
            available on a single sticker.
        target: The target string to be formed.

    Returns:
        The minimum number of stickers needed. Returns -1 if it is impossible.

    Examples:
        >>> solve([["a", "b", "c"], ["a", "d", "e"], ["c", "f"]], "abcd")
        2
        >>> solve([["a", "b", "c"], ["a", "d", "e"], ["c", "f"]], "abcde")
        2
        >>> solve([["a", "b", "c"], ["a", "d", "e"], ["c", "f"]], "xyz")
        -1
    """
    n = len(target)
    # target_masks maps each character to a bitmask representing its positions in target
    # Since target can have duplicate characters, we map each char to a list of bit positions
    char_to_target_indices: dict[str, list[int]] = {}
    for index, char in enumerate(target):
        if char not in char_to_target_indices:
            char_to_target_indices[char] = []
        char_to_target_indices[char].append(index)

    # Pre-process stickers into bitmasks relative to the target string
    # A sticker mask represents which indices of the target string this sticker can cover
    sticker_masks: list[int] = []
    for sticker in stickers:
        mask = 0
        sticker_set = set(sticker)
        for index, char in enumerate(target):
            if char in sticker_set:
                mask |= (1 << index)
        if mask > 0:
            sticker_masks.append(mask)

    # BFS to find the shortest path to the full mask (all bits set)
    # State: current bitmask of target characters covered
    # Goal: (1 << n) - 1
    target_mask = (1 << n) - 1
    queue: deque[tuple[int, int]] = deque([(0, 0)])  # (current_mask, count)
    visited: set[int] = {0}

    while queue:
        current_mask, count = queue.popleft()

        if current_mask == target_mask:
            return count

        # Optimization: Find the first character in the target not yet covered
        # This reduces the branching factor significantly by forcing the next sticker 
        # to cover a specific required character.
        first_uncovered_idx = 0
        while (current_mask >> first_uncovered_idx) & 1:
            first_uncovered_idx += 1
        
        target_char = target[first_uncovered_idx]

        # Only try stickers that contain the first uncovered character
        for s_mask in sticker_masks:
            # Check if this sticker covers the specific character we are looking for
            if (s_mask >> first_uncovered_idx) & 1:
                new_mask = current_mask | s_mask
                if new_mask not in visited:
                    visited.add(new_mask)
                    queue.append((new_mask, count + 1))

    return -1
