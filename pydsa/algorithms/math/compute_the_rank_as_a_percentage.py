METADATA = {
    "id": 2346,
    "name": "Compute the Rank as a Percentage",
    "slug": "compute_the_rank_as_a_percentage",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the percentage rank of each score based on its position in a sorted list of scores.",
}

def solve(scores: list[int]) -> list[int]:
    """
    Calculates the percentage rank for each score in the input list.
    
    The rank is calculated as: 100 * (number of scores > current_score + 1) / total_scores.
    Wait, the standard LeetCode definition for this specific problem (based on the prompt's logic) 
    is usually: 100 * (count of elements strictly greater than current) / total_elements.
    Actually, looking at the prompt's specific instruction: "Sort the scores and use the position 
    of the score to calculate the percentage rank."
    
    Standard Rank Percentage formula: 
    Rank = 100 * (count of elements > score) / total_elements
    
    Args:
        scores: A list of integers representing scores.
        
    Returns:
        A list of integers representing the percentage rank for each score.
        
    Examples:
        >>> solve([10, 20, 30, 40, 50])
        [80, 60, 40, 20, 0]
        >>> solve([5, 5, 5, 5])
        [0, 0, 0, 0]
    """
    n = len(scores)
    if n == 0:
        return []

    # Sort scores in descending order to easily find how many are strictly greater
    # However, to handle duplicates correctly and efficiently, we sort ascending
    # and use the index of the first occurrence of the score.
    sorted_scores = sorted(scores)
    
    # Map each unique score to its rank percentage.
    # The rank percentage is determined by how many elements are strictly greater than it.
    # If we sort ascending, the number of elements strictly greater than sorted_scores[i]
    # is (n - 1 - last_index_of_score). 
    # A more robust way: The number of elements strictly greater than 'x' is 
    # (n - index of first occurrence of 'x' from the right side).
    # Actually, the simplest way: count how many elements are > x.
    # In a sorted list, if we find the first index 'i' where sorted_scores[i] == x,
    # then there are (n - i) elements >= x. 
    # The number of elements strictly greater than x is (n - index_of_last_occurrence_of_x - 1)? No.
    # Let's use: count of elements > x is (n - index of first element > x).
    
    rank_map = {}
    
    # We iterate through the sorted list. For each unique score, 
    # the number of elements strictly greater than it is (n - index of first element > score).
    # Since the list is sorted, we can use binary search or a simple pointer.
    
    import bisect
    
    for score in set(scores):
        # bisect_right returns the index where 'score' could be inserted while maintaining order,
        # effectively giving the index of the first element strictly greater than 'score'.
        greater_count_index = bisect.bisect_right(sorted_scores, score)
        count_greater = n - greater_count_index
        
        # Calculate percentage: (count_greater * 100) // n
        # Note: The problem usually implies integer division or specific rounding.
        # Based on the prompt's logic: 100 * count_greater / n
        rank_map[score] = (count_greater * 100) // n

    # Construct the result list based on the original order
    return [rank_map[score] for score in scores]
