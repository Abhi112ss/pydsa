METADATA = {
    "id": 2350,
    "name": "Shortest Impossible Sequence of Rolls",
    "slug": "shortest-impossible-sequence-of-rolls",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Find the length of the shortest sequence of rolls that cannot be formed as a subsequence of the given rolls.",
}

def solve(rolls: list[int]) -> int:
    """
    Finds the length of the shortest sequence of rolls that cannot be formed 
    as a subsequence of the given rolls.

    The algorithm uses a greedy approach. To form a sequence of length 'k', 
    we must be able to find all possible values (1 to m) in a sequence of 
    disjoint segments within the rolls array. Each time we complete a full 
    set of all possible values (1 to m), we increment the length of the 
    sequence we can guarantee.

    Args:
        rolls: A list of integers representing the sequence of rolls.

    Returns:
        The length of the shortest impossible sequence.

    Examples:
        >>> solve([1, 4, 2, 3, 1, 3, 2, 4])
        3
        >>> solve([1, 1, 2, 2, 3, 3, 4, 4])
        2
    """
    # The problem implies rolls are in range [1, m]. 
    # However, the problem description for 2350 usually implies m is 
    # the number of unique values available. In the standard version, 
    # m is the number of distinct values present in the set of all possible rolls.
    # Since the problem doesn't explicitly give 'm', we must infer it.
    # Actually, in LeetCode 2350, 'm' is the number of distinct values 
    # that can be rolled. Looking at the constraints, m is the number of 
    # distinct elements in the set of all possible rolls. 
    # Wait, the problem states: "m is the number of distinct values".
    # Let's find the number of unique values in the input to determine m.
    # Actually, the problem implies m is the number of distinct values 
    # that *could* be rolled. In the context of this problem, m is the 
    # number of unique elements in the input.
    
    # Correction: The problem states m is the number of distinct values.
    # We can find m by checking the set of all elements.
    unique_elements = set(rolls)
    m = len(unique_elements)
    
    # If m is 0, the shortest impossible sequence is length 1.
    if not rolls:
        return 1

    # We track how many unique elements we have seen in the current "round".
    # A "round" is a segment of the array that contains all m distinct values.
    # Once a round is complete, we can definitely form any sequence of length 'current_length'.
    
    count_in_current_round = 0
    seen_in_current_round = set()
    possible_sequence_length = 1
    
    for roll in rolls:
        if roll not in seen_in_current_round:
            seen_in_current_round.add(roll)
            count_in_current_round += 1
            
            # If we have seen all m distinct values, we have completed a round.
            # This means we can extend the guaranteed sequence length by 1.
            if count_in_current_round == m:
                possible_sequence_length += 1
                # Reset for the next round
                seen_in_current_round = set()
                count_in_current_round = 0
                
    return possible_sequence_length
