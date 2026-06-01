METADATA = {
    "id": 3106,
    "name": "Lexicographically Smallest String After Operations With Constraint",
    "slug": "lexicographically-smallest-string-after-operations-with-constraint",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct the lexicographically smallest string by greedily picking the smallest character allowed by the constraints at each position.",
}

def solve(s: str, max_cost: int) -> str:
    """
    Constructs the lexicographically smallest string possible by modifying 
    the input string 's' such that the total cost of changes does not exceed 'max_cost'.
    The cost of changing a character from 'c1' to 'c2' is min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2))).

    Args:
        s: The input string.
        max_cost: The maximum allowed total cost for all character changes.

    Returns:
        The lexicographically smallest string achievable within the cost constraint.

    Examples:
        >>> solve("abc", 2)
        'aaa'
        >>> solve("abc", 0)
        'abc'
        >>> solve("z", 1)
        'a'
    """
    n = len(s)
    res = list(s)

    def get_cost(char_from: str, char_to: str) -> int:
        """Calculates the circular distance between two characters."""
        diff = abs(ord(char_from) - ord(char_to))
        return min(diff, 26 - diff)

    for i in range(n):
        current_char = s[i]
        # We want to change current_char to 'a' if possible to get the smallest string.
        # If 'a' is already the current char, no cost is incurred.
        if current_char == 'a':
            continue

        # Calculate the cost to change the current character to 'a'
        cost_to_a = get_cost(current_char, 'a')

        if cost_to_a <= max_cost:
            # If we can afford to change it to 'a', do it and subtract cost
            res[i] = 'a'
            max_cost -= cost_to_a
        else:
            # If we cannot afford 'a', we try to find the smallest character 'target'
            # such that the cost to change current_char to 'target' is within max_cost.
            # Since we want the lexicographically smallest, we check characters from 'a' upwards.
            # However, we only need to check characters that are smaller than current_char.
            # Actually, the greedy choice is to find the smallest char 'c' such that 
            # get_cost(current_char, c) <= max_cost.
            
            # Because we want the smallest possible character, we iterate through 'a', 'b', 'c'...
            # and pick the first one that satisfies the cost constraint.
            # Note: Since we couldn't reach 'a', we are looking for the smallest char in ['b', ..., current_char].
            # But wait, the cost function is circular. The smallest character might not be 'a'.
            # However, in a lexicographical sense, 'a' is always best. If we can't reach 'a',
            # we check 'b', then 'c', etc.
            
            found = False
            for char_code in range(ord('a'), ord(current_char)):
                target_char = chr(char_code)
                cost = get_cost(current_char, target_char)
                if cost <= max_cost:
                    res[i] = target_char
                    max_cost -= cost
                    found = True
                    break
            
            # If we couldn't find any character smaller than current_char within max_cost,
            # we keep current_char as is. (The loop above handles this).
            if not found:
                # We don't change res[i], it remains s[i]
                pass

    return "".join(res)
