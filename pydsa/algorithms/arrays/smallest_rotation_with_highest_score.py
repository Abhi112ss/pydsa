METADATA = {
    "id": 798,
    "name": "Smallest Rotation With Highest Score",
    "slug": "smallest-rotation-with-highest-score",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest rotation of an array that yields the maximum score based on adjacent element comparisons.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest rotation index that results in the maximum score.
    
    The score is calculated by summing 1 if nums[i] > nums[i+1], 
    -1 if nums[i] < nums[i+1], and 0 if they are equal.
    
    Args:
        nums: A list of integers representing the circular array.
        
    Returns:
        The smallest starting index of the rotation that achieves the maximum score.
        
    Examples:
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([4, 3, 2, 1])
        0
        >>> solve([1, 1, 1, 1])
        0
        >>> solve([1, 3, 2, 4])
        1
    """
    n = len(nums)
    if n <= 1:
        return 0

    # diff_array[i] will store the change in score when the rotation starts at index i.
    # We use a difference array to handle range updates in O(1).
    diff_array = [0] * (n + 1)

    for i in range(n):
        # Compare current element with the next element in a circular fashion
        curr_val = nums[i]
        next_val = nums[(i + 1) % n]

        if curr_val > next_val:
            # If nums[i] > nums[i+1], this pair contributes +1 to the score.
            # This pair contributes to all rotations where the 'break' (the gap between 
            # the last and first element of the rotation) is NOT between i and i+1.
            # Specifically, the pair (i, i+1) is part of the rotation if the rotation 
            # starts at index k such that k is in the range [i+2, i] (circularly).
            # More simply: the pair (i, i+1) is "broken" if the rotation starts at index i+1.
            # If the rotation starts at index i+1, the pair (i, i+1) becomes the (last, first) pair.
            # In a rotation starting at k, the pair (i, i+1) is internal if k != i+1.
            
            # Let's re-evaluate: A pair (i, i+1) contributes to the score if it is NOT the 
            # wrap-around pair. The wrap-around pair for rotation starting at k is (k-1, k).
            # So (i, i+1) contributes if k != i+1.
            
            # If curr > next, score += 1 for all k in [0, n-1] EXCEPT k = i+1.
            # However, we must also consider the wrap-around pair itself.
            # Let's use a simpler logic:
            # For each index i, calculate the contribution of the pair (i, (i+1)%n).
            # This pair contributes to the score of rotation k if the pair is NOT the wrap-around.
            # The wrap-around pair for rotation k is (k-1, k) [where k-1 is taken mod n].
            # So pair (i, (i+1)%n) is the wrap-around if k = (i+1)%n.
            
            # Total score for rotation k = sum_{j != k-1 mod n} score(j, j+1)
            # Let S = sum_{j=0 to n-1} score(j, (j+1)%n)
            # Score(k) = S - score(k-1, k)
            pass

    # Correct approach:
    # 1. Calculate the score of the original array (rotation 0).
    # 2. Calculate the score of every other rotation using the relationship:
    #    Score(k) = Score(k-1) - score(k-1, k) + score(k-1, k) is wrong.
    #    Actually, Score(k) is the sum of scores of pairs (j, j+1) where j is NOT k-1.
    
    # Let's pre-calculate the score of all adjacent pairs (i, (i+1)%n)
    pair_scores = [0] * n
    total_sum = 0
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            pair_scores[i] = 1
        elif nums[i] < nums[(i + 1) % n]:
            pair_scores[i] = -1
        else:
            pair_scores[i] = 0
        total_sum += pair_scores[i]

    # The score of rotation k is the sum of pair_scores[j] for all j 
    # such that the pair (j, j+1) is NOT the wrap-around pair.
    # The wrap-around pair for rotation k is (k-1, k).
    # So Score(k) = total_sum - pair_scores[k-1 mod n].
    
    max_score = float('-inf')
    best_idx = 0

    for k in range(n):
        # The pair that becomes the wrap-around for rotation k is (k-1) % n
        current_rotation_score = total_sum - pair_scores[(k - 1) % n]
        
        if current_rotation_score > max_score:
            max_score = current_rotation_score
            best_idx = k
        elif current_rotation_score == max_score:
            # We want the smallest index, and we are iterating k from 0 to n-1,
            # so the first one we encounter is already the smallest.
            pass

    return best_idx
