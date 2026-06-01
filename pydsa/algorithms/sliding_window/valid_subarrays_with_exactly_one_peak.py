METADATA = {
    "id": 3874,
    "name": "Valid Subarrays With Exactly One Peak",
    "slug": "valid_subarrays_with_exactly_one_peak",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays that contain exactly one peak element.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays that contain exactly one peak.
    A peak is defined as an element that is strictly greater than its neighbors.
    For boundary elements, they are peaks if they are strictly greater than their only neighbor.

    Args:
        nums: A list of integers.

    Returns:
        The total count of subarrays containing exactly one peak.

    Examples:
        >>> solve([1, 3, 2])
        3
        # Subarrays: [1, 3], [3, 2], [1, 3, 2] (all have peak 3)
        >>> solve([1, 2, 3, 2, 1])
        6
        # Subarrays: [1,2,3], [2,3], [3], [3,2], [3,2,1], [2,3,2] (all have peak 3)
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1

    total_peaks_subarrays = 0
    
    # We iterate through the array to find every local peak.
    # A peak at index i is defined as nums[i-1] < nums[i] > nums[i+1].
    # We must handle boundaries (index 0 and n-1) carefully.
    
    # To avoid double counting and ensure O(n), we identify the range 
    # where a specific peak is the *only* peak.
    # However, the problem asks for subarrays with EXACTLY one peak.
    # A more robust way: A subarray [L, R] has exactly one peak if there is 
    # exactly one index i in [L, R] such that i is a peak relative to [L, R].
    
    # Let's redefine: An index i is a peak in subarray [L, R] if:
    # 1. L < i < R and nums[i-1] < nums[i] > nums[i+1]
    # 2. i == L and i < R and nums[i] > nums[i+1]
    # 3. i == R and i > L and nums[i] > nums[i-1]
    # 4. L == i == R (single element subarray)

    # This is equivalent to saying the subarray is unimodal (increases then decreases).
    # A unimodal subarray has exactly one peak.
    
    # We can use a two-pointer/sliding window approach to find all maximal unimodal subarrays.
    # But a simpler way: Every unimodal subarray has exactly one peak.
    # We can iterate through each index i and treat it as the potential peak.
    # For a fixed peak i, we find the largest range [left, right] such that 
    # the sequence is strictly increasing from left to i and strictly decreasing from i to right.
    
    # However, the problem "Exactly one peak" usually implies the peak is a local maximum.
    # Let's find all indices that are peaks in the original array.
    # For each peak, we find how far we can extend left (decreasing) and right (decreasing).
    
    # Step 1: Identify all local peaks in the original array.
    # Step 2: For each peak, calculate the number of valid subarrays.
    # Note: A subarray might have a peak that wasn't a peak in the original array 
    # (e.g., [1, 2, 3] -> 3 is a peak in the subarray but not in the original if 3 < 4).
    # Actually, the standard definition of a peak in a subarray is relative to its boundaries.
    
    # Correct approach: A subarray has exactly one peak if it is unimodal.
    # A unimodal subarray consists of a strictly increasing part followed by a strictly decreasing part.
    
    # We use a sliding window to find maximal unimodal segments.
    # A segment is unimodal if it doesn't contain a "valley" (nums[i-1] > nums[i] < nums[i+1]).
    
    # Let's use the property: A subarray has exactly one peak if it does not contain 
    # any index i such that nums[i-1] >= nums[i] <= nums[i+1] (with strictness handled).
    # Actually, the simplest way to count unimodal subarrays:
    # A subarray is unimodal if it has no "valleys".
    # A valley is an index i where nums[i-1] >= nums[i] and nums[i] <= nums[i+1] 
    # (excluding the case where it's just a flat plateau, but the problem implies strict peaks).
    
    # Let's refine: A peak is an element strictly greater than its neighbors.
    # A subarray [i, j] has exactly one peak if there is exactly one k in [i, j] 
    # such that k is a peak in [i, j].
    
    # This is equivalent to: the subarray is strictly increasing then strictly decreasing.
    # Example: [1, 2, 3, 2, 1] -> Peak is 3.
    # Example: [1, 2, 3] -> Peak is 3.
    # Example: [3, 2, 1] -> Peak is 3.
    # Example: [1, 2, 2, 1] -> No peak (if strict).
    
    # Let's find all maximal strictly increasing then strictly decreasing segments.
    # A segment [L, R] is maximal unimodal if:
    # nums[L...peak] is strictly increasing and nums[peak...R] is strictly decreasing.
    
    # To avoid overcounting (e.g., [1, 2, 3] is part of [1, 2, 3, 2]), 
    # we can use the property that every unimodal subarray has a unique peak 
    # if we define the peak as the largest element. If there are multiple equal 
    # largest elements, it's not strictly unimodal.
    
    # Let's find all indices i that can be a peak.
    # For each i, find max L such that nums[L...i] is strictly increasing.
    # For each i, find max R such that nums[i...R] is strictly decreasing.
    # The number of unimodal subarrays with peak i is (i - L + 1) * (R - i + 1).
    # But we must subtract cases where the same subarray is counted for different peaks.
    # If we use strict inequality, each unimodal subarray has exactly one peak.
    
    # Wait, if the subarray is [1, 2, 3, 2, 1], peak is 3.
    # If the subarray is [1, 2, 3], peak is 3.
    # If the subarray is [3, 2, 1], peak is 3.
    # If the subarray is [1, 2, 2, 1], there is NO peak (no element is > neighbors).
    
    # So the algorithm is:
    # 1. For each index i, calculate:
    #    inc[i]: number of elements to the left of i (including i) such that they are strictly increasing to i.
    #    dec[i]: number of elements to the right of i (including i) such that they are strictly decreasing from i.
    # 2. A subarray with peak i is valid if it's within the range [i - inc[i] + 1, i + dec[i] - 1].
    # 3. The number of such subarrays is inc[i] * dec[i].
    # 4. However, we must ensure we don't count the same subarray twice.
    #    If a subarray has only one peak, it will be counted exactly once by its peak.
    #    If a subarray has no peak (like [1, 2, 2, 1]), it won't be counted.
    #    If a subarray has two peaks (like [1, 3, 1, 3, 1]), it will be counted twice.
    #    But the problem asks for subarrays with EXACTLY one peak.
    #    So we only want to count subarrays that have exactly one peak.
    #    Our method counts subarrays where 'i' is a peak.
    #    If a subarray has two peaks, it will be counted twice.
    #    Wait, if a subarray has two peaks, it is NOT a unimodal subarray.
    #    The question is: "Count subarrays with exactly one peak".
    #    If a subarray is [1, 3, 1, 3, 1], it has two peaks (index 1 and 3).
    #    Our algorithm would count [1, 3, 1] twice (once for peak at index 1, once for index 3).
    #    But the problem asks for subarrays with EXACTLY one peak.
    #    So we need to subtract the ones that have more than one peak? 
    #    No, the logic "count subarrays where i is the peak" is correct, 
    #    BUT we must ensure that the subarray we are counting doesn't contain OTHER peaks.
    
    # Let's refine:
    # A subarray [L, R] has exactly one peak if there is exactly one k in [L, R] 
    # such that k is a peak in [L, R].
    
    # Let's use the "maximal unimodal" approach.
    # A subarray is unimodal if it has exactly one peak.
    # A peak is an index i where nums[i-1] < nums[i] > nums[i+1] (with boundary rules).
    
    # Let's find all indices i that are peaks in the original array.
    # For each such i, find the largest range [L_i, R_i] such that i is the ONLY peak in [L_i, R_i].
    # This is still tricky.
    
    # Let's use the property: A subarray has exactly one peak if and only if 
    # it is strictly increasing then strictly decreasing.
    # Let's find all maximal strictly increasing then strictly decreasing segments.
    # A segment [start, end] is maximal if it cannot be extended.
    # Example: [1, 2, 3, 2, 1, 2, 3, 2, 1]
    # Maximal unimodal segments: [0, 4] (1,2,3,2,1) and [4, 8] (1,2,3,2,1).
    # Note they overlap at the "valley" or "end" point.
    
    # Actually, the simplest way to count subarrays with exactly one peak:
    # 1. Find all indices i that are peaks in the original array.
    # 2. For each peak i, find the largest range [L, R] such that i is the only peak in [L, R].
    #    The range [L, R] is bounded by the nearest peaks to the left and right.
    #    Wait, that's not enough. A subarray could have no peaks in the original array 
    #    but have a peak in itself (e.g., [1, 2, 3] in [1, 2, 3, 4]).
    
    # Let's use the definition: A peak in [L, R] is an index k in [L, R] such that:
    # (k == L or nums[k-1] < nums[k]) AND (k == R or nums[k] > nums[k+1])
    
    # Let's re-read: "Exactly one peak".
    # This is equivalent to: The subarray is unimodal.
    # A subarray is unimodal if it has a single local maximum.
    # This means it increases to a point and then decreases.
    # It cannot have a plateau (nums[i] == nums[i+1]) because then the peak wouldn't be strict.
    # Wait, if the array is [1, 2, 2, 1], is there a peak? 
    # No, because 2 is not > 2.
    # So the subarray must be strictly increasing then strictly decreasing.
    
    # Algorithm:
    # 1. Find all maximal strictly increasing segments.
    # 2. Find all maximal strictly decreasing segments.
    # 3. A unimodal subarray is formed by an increasing segment and a decreasing segment 
    #    that meet at a common peak.
    
    # Let's use the "peak-centric" approach:
    # For each index i:
    #   Let left[i] be the number of elements to the left such that nums[i-left[i]+1 ... i] is strictly increasing.
    #   Let right[i] be the number of elements to the right such that nums[i ... i+right[i]-1] is strictly decreasing.
    #   The number of unimodal subarrays with peak i is left[i] * right[i].
    #   Wait, this counts [1, 2, 3] as having peak 3.
    #   It counts [3, 2, 1] as having peak 3.
    #   It counts [1, 2, 3, 2, 1] as having peak 3.
    #   It counts [1, 2, 2, 1] as having NO peak.
    #   Does this overcount?
    #   If a subarray is [1, 2, 3, 2, 1], the only peak is 3. It's counted once.
    #   If a subarray is [1, 2, 3, 4, 3, 2, 1], the only peak is 4. It's counted once.
    #   If a subarray is [1, 2, 3, 2, 3, 2, 1], it has two peaks (3 and 3).
    #   The subarray [1, 2, 3, 2, 3] would be counted twice? 
    #   No, because for peak at index 2, the right side must be strictly decreasing.
    #   [1, 2, 3, 2, 3] is not strictly decreasing after index 2.
    #   So [1, 2, 3, 2, 3] is not counted for peak 2.
    #   Is [1, 2, 3, 2, 3] counted for peak 4? No, because the left side must be strictly increasing.
    #   [1, 2, 3, 2, 3] is not strictly increasing to index 4.
    #   Therefore, each unimodal subarray is counted EXACTLY once, by its unique peak.
    
    # Final Algorithm:
    # 1. For each i, find how many elements to the left are strictly increasing to i.
    # 2. For each i, find how many elements to the right are strictly decreasing from i.
    # 3. Sum (left[i] * right[i]) for all i.
    # 4. BUT, we must exclude the case where the "peak" is not actually a peak 
    #    in the context of the subarray? No, the definition of peak in a subarray 
    #    is exactly what we are using.
    #    Wait, there's one catch: a single element [5] is a peak.
    #    Our formula: left[0]=1, right[0]=1 -> 1*1 = 1. Correct.
    #    [1, 2, 3]:
    #    i=0: left=1, right=1 (if 1>2 is false) -> 1*1=1? No.
    #    Let's trace [1, 2, 3]:
    #    i=0: left=1, right=1 (since 1 < 2, right is 1) -> 1*1 = 1. Subarray [1].
    #    i=1: left=2 (1<2), right=1 (2<3) -> 2*1 = 2. Subarrays [2], [1, 2].
    #    i=2: left=3 (1<2<3), right=1 -> 3*1 = 3. Subarrays [3], [2, 3], [1, 2, 3].
    #    Total = 1 + 2 + 3 = 6.
    #    Wait, [1, 2, 3] has only ONE peak (3).
    #    Subarrays of [1, 2, 3]:
    #    [1]: peak 1.
    #    [2]: peak 2.
    #    [3]: peak 3.
    #    [1, 2]: peak 2.
    #    [2, 3]: peak 3.
    #    [1, 2, 3]: peak 3