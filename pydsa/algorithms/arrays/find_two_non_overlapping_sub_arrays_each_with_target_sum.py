METADATA = {
    "id": 1477,
    "name": "Find Two Non-overlapping Sub-arrays Each With Target Sum",
    "slug": "find-two-non-overlapping-sub-arrays-each-with-target-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find two non-overlapping subarrays that each sum up to a given target value.",
}

def solve(nums: list[int], target: int) -> list[list[int]]:
    """
    Finds two non-overlapping subarrays that each sum up to the target value.

    The algorithm uses a prefix sum approach combined with a hash map to track 
    the most recent index where a specific prefix sum occurred. It maintains 
    the 'best' (rightmost) end index of a valid subarray found so far to 
    ensure non-overlapping property when searching for the second subarray.

    Args:
        nums: A list of integers.
        target: The target sum for each subarray.

    Returns:
        A list containing two lists, where each inner list represents the 
        start and end indices [start, end] of a valid subarray. 
        Returns an empty list if no such subarrays exist.

    Examples:
        >>> solve([3, 4, 7, 2, 4], 7)
        [[0, 1], [2, 2]]
        >>> solve([1, 1, 1, 1, 1], 2)
        [[0, 1], [2, 3]]
    """
    n = len(nums)
    # prefix_sum_map stores the most recent index where a prefix sum was seen
    prefix_sum_map = {0: -1}
    current_sum = 0
    
    # last_valid_end stores the end index of the most recent valid subarray found
    # that ends before the current index.
    last_valid_end = -1
    first_subarray = []
    
    # We iterate through the array once to find the first valid subarray 
    # and store its end index.
    # To handle the "non-overlapping" constraint efficiently, we can 
    # think of this as finding the first subarray that ends at or before i,
    # and then finding a second subarray that starts after that.
    
    # However, a more robust way is to find the "earliest" possible end 
    # for the first subarray to leave maximum room for the second.
    
    # Let's refine: We need to find two subarrays. 
    # We can track the end index of the most recent valid subarray found.
    # If we find a new valid subarray, we check if it's possible to have 
    # a previous valid subarray that ended before this one started.
    
    # To do this in one pass, we store the end index of the most recent 
    # valid subarray found so far.
    
    found_first = False
    first_sub_indices = []
    
    # We will use a two-pass logic or a single pass with a "best end" tracker.
    # Let's use the "best end" tracker:
    # 'last_end_of_first_subarray' will store the end index of the first 
    # subarray found that allows for a second one.
    
    # Actually, the simplest O(n) way:
    # 1. Find all valid subarrays and their [start, end].
    # 2. For each valid subarray [s2, e2], check if there exists a 
    #    valid subarray [s1, e1] such that e1 < s2.
    
    # To do this in O(n), we keep track of the end index of the 
    # "most recent" valid subarray found.
    
    valid_subarrays_end_indices = [] # stores (start, end)
    
    # First pass: find all valid subarrays
    current_sum = 0
    prefix_sum_map = {0: -1}
    
    # We'll store the end index of the most recent valid subarray found 
    # that ends before the current index.
    # latest_valid_end_index: the end index of a valid subarray found so far.
    # latest_valid_start_index: the start index of that subarray.
    latest_valid_end_index = -1
    latest_valid_start_index = -1
    
    for i in range(n):
        current_sum += nums[i]
        needed = current_sum - target
        
        if needed in prefix_sum_map:
            start_idx = prefix_sum_map[needed] + 1
            end_idx = i
            
            # If this is the second subarray we found, and it starts 
            # after the previous one ended, we are done.
            if latest_valid_end_index != -1 and start_idx > latest_valid_end_index:
                return [[latest_valid_start_index, latest_valid_end_index], [start_idx, end_idx]]
            
            # Otherwise, update the "latest" valid subarray found.
            # We want the one that ends as early as possible to maximize 
            # chances for the second one, but since we are iterating 
            # linearly, the first one we find that satisfies the condition 
            # is naturally the one that ends earliest.
            if latest_valid_end_index == -1:
                latest_valid_end_index = end_idx
                latest_valid_start_index = start_idx
            else:
                # If we already found a valid subarray, we only update 
                # 'latest' if the new one ends earlier? No, because 
                # we want to find the first pair. The first pair we 
                # encounter where start_idx > latest_valid_end_index 
                # is guaranteed to be a valid non-overlapping pair.
                # However, we should update latest_valid_end_index 
                # only if the new one ends EARLIER than the current 
                # latest_valid_end_index to leave more room.
                if end_idx < latest_valid_end_index:
                    latest_valid_end_index = end_idx
                    latest_valid_start_index = start_idx
                    
        prefix_sum_map[current_sum] = i
        
    return []
