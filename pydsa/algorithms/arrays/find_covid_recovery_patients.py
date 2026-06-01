METADATA = {
    "id": 3586,
    "name": "Find COVID Recovery Patients",
    "slug": "find_covid_recovery_patients",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of patients who transitioned from an infected state to a recovered state within a specific observation window.",
}

def solve(patient_states: list[int], recovery_threshold: int) -> int:
    """
    Calculates the number of patients who transitioned from infected (1) 
    to recovered (0) within a sliding window of size recovery_threshold.

    Args:
        patient_states: A list of integers where 1 represents infected 
            and 0 represents recovered.
        recovery_threshold: The size of the observation window.

    Returns:
        The count of unique recovery transitions (1 -> 0) found within 
        any window of the given threshold size.

    Examples:
        >>> solve([1, 1, 0, 1, 0, 0], 3)
        2
        >>> solve([0, 0, 0], 2)
        0
        >>> solve([1, 0, 1, 0], 2)
        2
    """
    n = len(patient_states)
    if n < 2 or recovery_threshold < 2:
        return 0

    # A transition is defined as a pair (i, i+1) where states[i] == 1 and states[i+1] == 0.
    # We need to find how many such transitions exist within any window of size 'recovery_threshold'.
    # However, the problem asks for the total count of such transitions that occur.
    # If the window slides, we are looking for the number of indices 'i' such that 
    # patient_states[i] == 1 and patient_states[i+1] == 0, 
    # and both i and i+1 fall within a window of size 'recovery_threshold'.
    
    # Since any transition (i, i+1) is contained in a window of size K if K >= 2,
    # and the problem asks for the count of such transitions, we simply iterate 
    # through the array and check the condition.
    
    recovery_count = 0
    
    # We iterate up to n-1 because a transition requires two adjacent elements.
    for i in range(n - 1):
        # Check if the current patient is infected and the next is recovered
        if patient_states[i] == 1 and patient_states[i + 1] == 0:
            # A transition (i, i+1) is valid if it fits in the window.
            # In a standard sliding window problem of this type, we count 
            # how many such events occur.
            recovery_count += 1
            
    return recovery_count
