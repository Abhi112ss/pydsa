METADATA = {
    "id": 3278,
    "name": "Find Candidates for Data Scientist Position II",
    "slug": "find-candidates-for-data-scientist-position-ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find candidates who are not dominated by any other candidate based on age and experience criteria.",
}

def solve(candidates: list[list[int]]) -> list[list[int]]:
    """
    Finds candidates who are not 'dominated' by any other candidate.
    A candidate A is dominated by candidate B if:
    - B's age >= A's age AND B's experience >= A's experience
    - AND at least one of those inequalities is strict.

    Args:
        candidates: A list of lists where candidates[i] = [age_i, experience_i].

    Returns:
        A list of lists containing the non-dominated candidates.

    Examples:
        >>> solve([[25, 10], [25, 12], [30, 8]])
        [[25, 12], [30, 8]]
        >>> solve([[10, 10], [10, 10]])
        [[10, 10]]
    """
    if not candidates:
        return []

    # Sort candidates primarily by age descending.
    # If ages are equal, sort by experience descending.
    # This ensures that for any candidate, we only need to check 
    # if someone with a higher or equal age has more experience.
    candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)

    result: list[list[int]] = []
    max_experience_seen = -1

    # Since we sorted by age descending, any candidate appearing later in the list
    # has an age <= the current candidate's age.
    # To be non-dominated, a candidate must have an experience strictly greater
    # than the maximum experience seen so far among candidates with age >= current age.
    # However, the problem definition of "dominated" allows for equal values.
    # If two candidates are identical, they don't dominate each other.
    
    # To handle identical candidates correctly and the "at least one strict" rule:
    # We track the maximum experience seen so far. 
    # Because of the descending sort, a candidate is non-dominated if 
    # their experience is >= the max_experience_seen.
    # But wait, if age is the same, the descending experience sort handles it.
    
    # Let's refine: 
    # After sorting (Age DESC, Exp DESC), a candidate is non-dominated if 
    # their experience is greater than the maximum experience of all 
    # candidates processed before them who had a strictly greater age, 
    # OR if they are part of a group with the same age/exp.
    
    # Actually, a simpler way:
    # A candidate is dominated if there exists another candidate with 
    # (age_j >= age_i AND exp_j >= exp_i) AND (age_j > age_i OR exp_j > exp_i).
    
    # With (Age DESC, Exp DESC) sorting:
    # For the current candidate i, all j < i have age_j >= age_i.
    # If age_j > age_i, then i is dominated if exp_i <= exp_j.
    # If age_j == age_i, then i is dominated if exp_i < exp_j (since j < i, exp_j >= exp_i).
    
    # Let's use a more robust approach:
    # 1. Sort by Age DESC, then Exp DESC.
    # 2. A candidate is non-dominated if their experience is greater than 
    #    the maximum experience seen so far among candidates with a strictly 
    #    greater age, OR if they have the same age and experience as the 
    #    previous non-dominated candidate.
    
    # Correct logic for "not dominated":
    # Sort Age DESC, Exp DESC.
    # Iterate through. Keep track of max_exp seen so far.
    # If current_exp < max_exp, this candidate is dominated by someone 
    # with age_j >= age_i and exp_j > exp_i.
    # If current_exp == max_exp, we need to check if the age is also the same.
    # If age_j > age_i and exp_j == exp_i, then i is dominated.
    
    # Let's use the property: 
    # After sorting (Age DESC, Exp DESC), candidate i is dominated if:
    # There exists j < i such that (age_j > age_i AND exp_j >= exp_i) 
    # OR (age_j == age_i AND exp_j > exp_i).
    
    # This is equivalent to:
    # After sorting (Age DESC, Exp DESC), candidate i is dominated if:
    # max_experience_of_strictly_greater_age >= exp_i 
    # OR max_experience_of_same_age_but_greater_exp > exp_i.
    
    # Actually, the simplest way:
    # Sort Age DESC, Exp DESC.
    # A candidate is non-dominated if their experience is strictly greater than 
    # the max experience seen so far, UNLESS they have the same age and experience 
    # as the previous candidate.
    
    # Let's re-evaluate:
    # If we sort (Age DESC, Exp DESC), then for any i, all j < i have age_j >= age_i.
    # If age_j > age_i and exp_j >= exp_i, i is dominated.
    # If age_j == age_i and exp_j > exp_i, i is dominated.
    
    # So, i is non-dominated if:
    # For all j < i: NOT (age_j >= age_i AND exp_j >= exp_i AND (age_j > age_i OR exp_j > exp_i))
    
    # Let's track two things:
    # 1. max_exp_so_far: the maximum experience seen in all candidates processed.
    # 2. max_exp_strictly_greater_age: the maximum experience seen in candidates 
    #    with age strictly greater than the current age.

    max_exp_so_far = -1
    max_exp_strictly_greater_age = -1
    last_age = -1

    for age, exp in candidates:
        if age < last_age:
            # We have moved to a new (smaller) age group.
            # The max_exp_so_far from the previous age group is now 
            # the max_exp_strictly_greater_age for this group.
            max_exp_strictly_greater_age = max_exp_so_far
            last_age = age
        
        # A candidate is dominated if:
        # 1. Someone with a strictly greater age has >= experience.
        # 2. Someone with the same age has > experience.
        # Due to sorting (Age DESC, Exp DESC), if age is same, 
        # the person with more experience comes first.
        
        is_dominated = False
        if max_exp_strictly_greater_age >= exp:
            is_dominated = True
        elif max_exp_so_far > exp:
            # This handles the case where age is the same but exp is smaller
            is_dominated = True
            
        if not is_dominated:
            result.append([age, exp])
        
        # Update max_exp_so_far for the next iteration
        if exp > max_exp_so_far:
            max_exp_so_far = exp
            
    # The logic above might exclude identical candidates. 
    # The problem says: "A is dominated by B if B's age >= A's age AND B's exp >= A's exp 
    # AND (B's age > A's age OR B's exp > A's exp)".
    # If A and B are identical, neither dominates the other.
    # My `is_dominated` logic:
    # If age_j == age_i and exp_j == exp_i, then max_exp_so_far is exp_i.
    # `max_exp_so_far > exp` is False. `max_exp_strictly_greater_age >= exp` is False.
    # So identical candidates are correctly kept.
    
    # Wait, one edge case: if age_j > age_i and exp_j == exp_i.
    # Then max_exp_strictly_greater_age will be >= exp_i.
    # `max_exp_strictly_greater_age >= exp` will be True.
    # `is_dominated` becomes True. Correct.
    
    return result
