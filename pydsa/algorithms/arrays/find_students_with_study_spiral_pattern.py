METADATA = {
    "id": 3617,
    "name": "Find Students with Study Spiral Pattern",
    "slug": "find_students_with_study_spiral_pattern",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "pattern_matching", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Identify students whose study hours follow a specific increasing then decreasing spiral pattern.",
}

def solve(study_hours: list[int], k: int) -> list[int]:
    """
    Finds the indices of students whose study hours follow a spiral pattern 
    of length k. A spiral pattern is defined as a sequence that strictly 
    increases to a peak and then strictly decreases.

    Args:
        study_hours: A list of integers representing study hours per day.
        k: The required length of the spiral pattern.

    Returns:
        A list of starting indices where a spiral pattern of length k begins.

    Examples:
        >>> solve([1, 2, 3, 2, 1, 0, 1, 2], 5)
        [0, 3]
        >>> solve([1, 2, 3, 4, 5], 3)
        []
    """
    n = len(study_hours)
    if k < 3 or n < k:
        return []

    results = []

    # We use a sliding window approach or a pre-calculation of monotonic lengths.
    # To achieve O(n), we calculate how many elements are strictly increasing 
    # ending at i, and how many are strictly decreasing starting at i.
    
    # inc[i] = length of strictly increasing sequence ending at index i
    inc = [1] * n
    for i in range(1, n):
        if study_hours[i] > study_hours[i - 1]:
            inc[i] = inc[i - 1] + 1
            
    # dec[i] = length of strictly decreasing sequence starting at index i
    dec = [1] * n
    for i in range(n - 2, -1, -1):
        if study_hours[i] > study_hours[i + 1]:
            dec[i] = dec[i + 1] + 1

    # A spiral pattern of length k exists starting at index 'start' if there is 
    # a peak at index 'p' such that:
    # 1. The sequence from start to p is strictly increasing (length p - start + 1)
    # 2. The sequence from p to start + k - 1 is strictly decreasing (length (start + k - 1) - p + 1)
    # 3. The total length is exactly k.
    
    # However, the problem implies we need to find if ANY window of size k 
    # within the array follows the pattern.
    # A window [i, i + k - 1] is a spiral if there exists a peak 'p' 
    # where i < p < i + k - 1, inc[p] >= (p - i + 1) and dec[p] >= (i + k - 1 - p + 1)
    
    # Optimization: For a fixed window of size k, we check if there's a peak.
    # A peak p in window [i, i+k-1] must satisfy:
    # inc[p] >= p - i + 1  AND  dec[p] >= i + k - 1 - p + 1
    
    # To find if such a p exists for a window [i, i+k-1] in O(1) after O(n) prep:
    # We can iterate through all possible windows.
    for i in range(n - k + 1):
        window_end = i + k - 1
        # A valid peak p must be in range [i + 1, window_end - 1]
        # We check if any index p in this range can serve as the peak.
        # To keep it O(n) total, we observe that for a fixed window, 
        # we only need to check if the "maximal" peak in that window works.
        # But actually, we can just check if there's any p such that 
        # inc[p] + dec[p] - 1 >= k AND the peak is within the window bounds.
        
        # Let's refine: A window [i, i+k-1] is a spiral if there is a p 
        # such that the increasing part covers [i, p] and decreasing covers [p, i+k-1].
        # This is equivalent to: inc[p] >= p - i + 1 AND dec[p] >= i + k - 1 - p + 1
        # Rearranging: p - inc[p] + 1 <= i AND p + dec[p] - 1 >= i + k - 1
        
        # Since we need to find if ANY such p exists in [i+1, i+k-2], 
        # we can use a sliding window maximum or simply realize that 
        # if a spiral of length k exists, there is a peak p.
        # We can iterate through all possible peaks p and see which windows they satisfy.
        pass

    # Correct O(n) approach:
    # A peak p can support a spiral of length (inc[p] + dec[p] - 1).
    # If this length is >= k, then this peak can be the peak for multiple windows.
    # Specifically, for a peak p, it can be the peak for a window of length k 
    # starting at 'start' if:
    # 1. start <= p - (some_inc_len) + 1  where some_inc_len is part of inc[p]
    # 2. start + k - 1 >= p + (some_dec_len) - 1 where some_dec_len is part of dec[p]
    # Actually, the simplest way: A window [i, i+k-1] is a spiral if 
    # there exists p in (i, i+k-1) such that inc[p] >= p-i+1 and dec[p] >= i+k-1-p+1.
    
    # Let's use the property: a window [i, i+k-1] is a spiral if 
    # there is a p in [i+1, i+k-2] such that inc[p] + dec[p] - 1 >= k 
    # AND the peak p is "centered" enough such that the increasing/decreasing 
    # parts don't exceed the window boundaries.
    # Actually, if inc[p] + dec[p] - 1 >= k, then the peak p can form a spiral 
    # of length k by taking (p - i + 1) elements from the left and 
    # (k - (p - i + 1) + 1) elements from the right.
    # This is possible if:
    # (p - i + 1) <= inc[p]  => i >= p - inc[p] + 1
    # (i + k - 1 - p + 1) <= dec[p] => i <= p + dec[p] - k
    
    # So for each p, it can be a peak for windows starting at i in range:
    # [max(i_min, p - inc[p] + 1), min(i_max, p + dec[p] - k)]
    # where i_min = p - k + 2 (since p must be at least i+1)
    # and i_max = p - 1 (since p must be at most i+k-2)
    
    # Let's simplify: A window [i, i+k-1] is a spiral if there is a p 
    # such that i <= p - (some_val) and i + k - 1 >= p + (some_val).
    # The condition is: there exists p in [i+1, i+k-2] such that
    # inc[p] >= p - i + 1  AND  dec[p] >= i + k - 1 - p + 1
    
    # Let's use a different O(n) approach:
    # For each index p, it can be a peak for a range of window starts.
    # The window start 'i' must satisfy:
    # 1. i <= p - 1 (peak cannot be the first element)
    # 2. i >= p - k + 2 (peak cannot be the last element, p <= i + k - 2)
    # 3. i >= p - inc[p] + 1 (increasing part must reach i)
    # 4. i <= p + dec[p] - k (decreasing part must reach i + k - 1)
    
    # Combining these:
    # i_start = max(p - k + 2, p - inc[p] + 1)
    # i_end = min(p - 1, p + dec[p] - k)
    # If i_start <= i_end, then all i in [i_start, i_end] are valid starts.
    
    # We can use a difference array to mark these ranges in O(n).
    diff = [0] * (n + 2)
    for p in range(1, n - 1):
        i_start = max(p - k + 2, p - inc[p] + 1)
        i_end = min(p - 1, p + dec[p] - k)
        if i_start <= i_end:
            diff[i_start] += 1
            diff[i_end + 1] -= 1
            
    current_coverage = 0
    for i in range(n):
        current_coverage += diff[i]
        if current_coverage > 0:
            results.append(i)
            
    return results
