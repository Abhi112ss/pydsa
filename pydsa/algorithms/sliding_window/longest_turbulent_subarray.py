METADATA = {
    "id": 978,
    "name": "Longest Turbulent Subarray",
    "slug": "longest_turbulent_subarray",
    "category": "Arrays",
    "aliases": [],
    "tags": ["dp", "arrays", "sliding window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray such that the comparison sign between consecutive elements alternates.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the length of the longest subarray where the comparison sign 
    between consecutive elements alternates.

    Args:
        arr: A list of integers.

    Returns:
        The length of the longest turbulent subarray.

    Examples:
        >>> solve([9, 4, 2, 10, 7, 8, 8, 1, 9])
        5
        >>> solve([4, 8, 12, 16])
        2
        >>> solve([100])
        1
    """
    n = len(arr)
    if n < 2:
        return n

    max_length = 1
    # current_len tracks the length of the current turbulent window
    current_len = 0

    for i in range(n - 1):
        # Determine the relationship between current and next element
        # We use signum-like logic: 1 if a < b, -1 if a > b, 0 if a == b
        if arr[i] < arr[i + 1]:
            current_sign = 1
        elif arr[i] > arr[i + 1]:
            current_sign = -1
        else:
            current_sign = 0

        if current_sign != 0:
            # If this is the start of a new turbulent sequence
            if current_len == 0:
                current_len = 2
            # If the sign alternates compared to the previous pair
            elif (arr[i-1] < arr[i] and arr[i] > arr[i+1]) or \
                 (arr[i-1] > arr[i] and arr[i] < arr[i+1]):
                # Note: The logic above is slightly complex to handle the first pair.
                # A cleaner way is to track the previous sign.
                pass 
            
            # Let's refine the sliding window logic for clarity:
            # We'll use a more robust approach below.
            pass

    # Re-implementing with a cleaner sliding window approach
    max_length = 1
    anchor = 0
    
    for i in range(1, n):
        # Check if the current pair breaks the turbulence
        # A pair is turbulent if it's not equal.
        # A sequence is turbulent if signs alternate.
        
        # We compare the sign of (arr[i-1], arr[i]) with (arr[i], arr[i+1])
        # But it's easier to check if the current sign is the opposite of the previous sign.
        
        # Let's use the property: sign(arr[i]-arr[i-1]) == -sign(arr[i+1]-arr[i])
        pass

    # Final robust implementation
    max_len = 1
    current_len = 0
    
    for i in range(1, n):
        # Calculate sign of current pair
        if arr[i-1] < arr[i]:
            current_sign = 1
        elif arr[i-1] > arr[i]:
            current_sign = -1
        else:
            current_sign = 0
            
        if current_sign == 0:
            # Reset window if elements are equal
            current_len = 0
        elif i > 1 and current_sign == -prev_sign:
            # Increment if sign alternates
            current_len += 1
        else:
            # Start new window (length 2 because we have a valid pair)
            current_len = 1
            
        # If current_sign is not 0, the window includes at least 2 elements
        # current_len represents the number of 'edges' that satisfy the condition
        # The number of elements is current_len + 1
        if current_sign != 0:
            # If we just started a sequence, current_len is 1 (representing 1 edge)
            # If we are continuing, we add 1 to the edge count
            if i > 1 and current_sign == -prev_sign:
                current_len += 1
            else:
                current_len = 1
            
            max_len = max(max_len, current_len + 1)
            
        prev_sign = current_sign

    return max_len

def solve_optimized(arr: list[int]) -> int:
    """
    Optimized O(n) time and O(1) space implementation using a sliding window.
    """
    n = len(arr)
    if n < 2:
        return n

    max_len = 1
    # left is the start of the current turbulent window
    left = 0
    
    for right in range(1, n):
        # Check if the current pair is valid (not equal)
        # and if it maintains the alternating pattern
        is_alternating = False
        if right > 1:
            # Check if sign of (arr[right-2], arr[right-1]) is opposite of (arr[right-1], arr[right])
            prev_diff = arr[right-1] - arr[right-2]
            curr_diff = arr[right] - arr[right-1]
            if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
                is_alternating = True
        
        # If the current pair is equal, the window must reset to the current index
        if arr[right] == arr[right-1]:
            left = right
        # If the pattern is broken (not alternating and not equal), 
        # the window resets to the previous element
        elif not is_alternating and right > 1:
            # We check if the current pair itself is valid (not equal)
            # If it is, the new window starts at right-1
            left = right - 1
            
        # The window [left, right] is turbulent
        # However, we must ensure the window actually contains a valid pair
        # If arr[right] == arr[right-1], the window is just [right, right]
        # If they are not equal, the window is at least [right-1, right]
        if arr[right] != arr[right-1]:
            # If it's not alternating, the window is just the last two elements
            # unless it's the very first pair.
            if not is_alternating and right > 1:
                # We already set left = right - 1
                pass
            
            # If it is alternating, the window expands
            # If it's the first pair, left is 0, right is 1, len is 2
            max_len = max(max_len, right - left + 1)
            
    return max_len

# The actual production-grade implementation
def solve(arr: list[int]) -> int:
    """
    Finds the length of the longest turbulent subarray.

    Args:
        arr: A list of integers.

    Returns:
        The length of the longest turbulent subarray.
    """
    n = len(arr)
    if n < 2:
        return n

    max_len = 1
    # current_len tracks the number of consecutive elements in the current turbulent window
    current_len = 1
    # prev_sign stores the sign of the previous comparison: 1, -1, or 0
    prev_sign = 0

    for i in range(1, n):
        # Calculate sign of the current pair
        if arr[i] > arr[i-1]:
            curr_sign = 1
        elif arr[i] < arr[i-1]:
            curr_sign = -1
        else:
            curr_sign = 0

        if curr_sign == 0:
            # Elements are equal, reset window to a single element
            current_len = 1
        elif curr_sign == -prev_sign:
            # Sign alternates, extend the current window
            current_len += 1
        else:
            # Sign is the same as previous or it's the first valid pair
            # The window now consists of the previous element and the current one
            current_len = 2
            
        # Update max_len if current window is larger
        # Note: if curr_sign is 0, current_len is 1, which doesn't affect max_len >= 1
        if curr_sign != 0:
            max_len = max(max_len, current_len)
            
        prev_sign = curr_sign

    return max_len