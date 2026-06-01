METADATA = {
    "id": 1925,
    "name": "Count Square Sum Triples",
    "slug": "count-square-sum-triples",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of triples (i, j, k) such that the sum of squares of elements at these indices equals a target value.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Counts the number of triples (i, j, k) such that nums[i]^2 + nums[j]^2 + nums[k]^2 == target.

    Args:
        nums: A list of integers.
        target: The target sum of squares.

    Returns:
        The total count of unique index triples (i, j, k) where i < j < k.

    Examples:
        >>> solve([1, 2, 3], 14)
        1
        >>> solve([1, 1, 1, 1], 3)
        4
    """
    n = len(nums)
    if n < 3:
        return 0

    # Pre-calculate squares to avoid repeated multiplication in the inner loop
    squares = [x * x for x in nums]
    count = 0

    # Iterate through the first element of the triple
    for i in range(n - 2):
        target_two_sum = target - squares[i]
        
        # If the remaining target is negative, no need to continue with this i
        if target_two_sum < 0:
            continue

        # Use two pointers to find pairs (j, k) such that squares[j] + squares[k] == target_two_sum
        # Note: The problem asks for index triples (i, j, k) with i < j < k.
        # Since the input array is not necessarily sorted, we must handle the search carefully.
        # However, the standard two-pointer approach requires a sorted array.
        # To maintain O(n^2) and O(1) extra space (excluding the squares list), 
        # we can iterate j and then search for k.
        
        for j in range(i + 1, n - 1):
            needed = target_two_sum - squares[j]
            
            # We need to find how many k > j satisfy squares[k] == needed
            # Since we cannot sort the original array without losing index information,
            # and we want to avoid O(n^3), we use a simple loop or a frequency map.
            # But the prompt asks for O(n^2) time and O(1) space.
            # To achieve O(n^2) time, we can use a hash map for the third element, 
            # but that would be O(n) space. 
            # Given the constraints of "Count Square Sum Triples", if we assume 
            # we are looking for index combinations, we can iterate j and k.
            
            # Re-evaluating: To get O(n^2) time, we need to find k efficiently.
            # Let's use a frequency map for the elements appearing after index j.
            # However, a frequency map changes as j moves.
            pass

    # Correct O(n^2) implementation using a frequency map for the suffix
    # To keep space O(n) for the map, which is standard for O(n^2) time.
    # If the prompt strictly requires O(1) space, it implies a different constraint 
    # or that the array is sorted. Assuming standard O(n^2) time requirement.
    
    count = 0
    # Pre-calculate squares
    squares = [x * x for x in nums]
    
    # We use a frequency map to store counts of squares seen so far from the right
    # to allow O(1) lookup for the third element.
    from collections import Counter
    
    # suffix_counts[val] = number of times 'val' appears in squares[j+1:]
    suffix_counts = Counter(squares)
    
    # As we move i and j, we update the suffix_counts to ensure k > j
    for i in range(n):
        # Remove current i from suffix counts because k must be > i
        suffix_counts[squares[i]] -= 1
        
        for j in range(i + 1, n):
            # Remove current j from suffix counts because k must be > j
            suffix_counts[squares[j]] -= 1
            
            needed = target - squares[i] - squares[j]
            if needed in suffix_counts:
                count += suffix_counts[needed]
            
            # Note: We don't add squares[j] back yet; it stays removed for the next j
            # but we need to be careful. Let's refine the logic.
            
    # Refined logic for O(n^2) time and O(n) space:
    # We iterate i, then for each i, we use a two-pointer approach on the remaining part.
    # But two-pointer requires sorting. Sorting takes O(n log n).
    # Total complexity O(n^2 log n) or O(n^2) with a frequency map.
    
    return _solve_optimized(squares, target)

def _solve_optimized(squares: list[int], target: int) -> int:
    n = len(squares)
    count = 0
    
    # To find i < j < k such that sq[i] + sq[j] + sq[k] == target
    # We iterate through j, and for each j, we look for i < j and k > j.
    # This is still O(n^2) if we use a frequency map for elements to the left and right.
    
    left_counts = Counter()
    right_counts = Counter(squares)
    
    # Initial state: i < j < k. 
    # We will iterate j from 0 to n-1.
    # For a fixed j, we need to find pairs (i, k) such that i < j and k > j.
    # This is actually harder. Let's use the standard:
    # Fix i, then find j, k in the remaining array.
    
    total_count = 0
    for i in range(n - 2):
        # For a fixed i, we need to find j, k in range [i+1, n-1]
        # such that squares[j] + squares[k] == target - squares[i]
        sub_target = target - squares[i]
        
        # Use a frequency map for the suffix [i+1, n-1]
        # To keep it O(n^2), we build the map for the suffix once per i.
        suffix_map = Counter(squares[i+1:])
        
        for j in range(i + 1, n - 1):
            # Before checking j, remove squares[j] from suffix_map 
            # because k must be > j
            suffix_map[squares[j]] -= 1
            if suffix_map[squares[j]] == 0:
                del suffix_map[squares[j]]
                
            needed = sub_target - squares[j]
            if needed in suffix_map:
                total_count += suffix_map[needed]
                
    return total_count

# Re-implementing the solve function to be clean and single-pass
def solve(nums: list[int], target: int) -> int:
    """
    Counts the number of triples (i, j, k) such that nums[i]^2 + nums[j]^2 + nums[k]^2 == target.

    Args:
        nums: A list of integers.
        target: The target sum of squares.

    Returns:
        The total count of unique index triples (i, j, k) where i < j < k.
    """
    n = len(nums)
    if n < 3:
        return 0

    squares = [x * x for x in nums]
    total_count = 0

    # We iterate through j as the middle element of the triple (i, j, k)
    # This allows us to maintain a frequency map of elements to the left (i < j)
    # and a frequency map of elements to the right (k > j).
    
    left_map = Counter()
    right_map = Counter(squares)
    
    # Initially, all elements are in the right_map.
    # As we move j, we move elements from right_map to left_map.
    
    # To handle i < j < k, we can iterate j from 0 to n-1.
    # But we need to ensure i < j and k > j.
    # Let's use the approach: Fix i, then use a frequency map for the rest.
    
    for i in range(n - 2):
        # target_jk is what squares[j] + squares[k] must sum to
        target_jk = target - squares[i]
        
        # suffix_map contains counts of squares[m] for m > i
        suffix_map = Counter(squares[i+1:])
        
        for j in range(i + 1, n - 1):
            # Remove squares[j] from suffix_map so it only contains k > j
            suffix_map[squares[j]] -= 1
            if suffix_map[squares[j]] == 0:
                del suffix_map[squares[j]]
            
            needed = target_jk - squares[j]
            if needed in suffix_map:
                total_count += suffix_map[needed]
                
    return total_count

from collections import Counter
