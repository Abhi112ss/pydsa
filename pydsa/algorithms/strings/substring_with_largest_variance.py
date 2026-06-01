METADATA = {
    "id": 2272,
    "name": "Substring With Largest Variance",
    "slug": "substring-with-largest-variance",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["kadane_algorithm", "sliding_window", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum variance of any substring, where variance is the difference between the most and least frequent characters.",
}

def solve(s: str) -> int:
    """
    Finds the maximum variance of any substring in the given string.

    The variance is defined as the difference between the frequency of the 
    most frequent character and the least frequent character in the substring.
    A substring must contain at least one occurrence of the least frequent character.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The maximum variance found in any substring.

    Examples:
        >>> solve("xyxyy")
        2
        >>> solve("xyx")
        1
    """
    n = len(s)
    if n == 0:
        return 0

    # Count total occurrences of each character in the string
    # This helps us know if a character exists in the string at all
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    unique_chars = list(char_counts.keys())
    max_variance = 0

    # We iterate through every possible pair of (most_frequent, least_frequent) characters.
    # Since there are at most 26 characters, this is 26 * 25 = 650 iterations (O(1)).
    for most_frequent in unique_chars:
        for least_frequent in unique_chars:
            if most_frequent == least_frequent:
                continue
            
            # If the least_frequent character doesn't exist in the string, skip
            if char_counts[least_frequent] == 0:
                continue

            # We use a variation of Kadane's algorithm.
            # We want to maximize: (count of most_frequent) - (count of least_frequent)
            # However, we must ensure at least one least_frequent character is included.
            
            current_variance = 0
            # has_least tracks if the current window contains at least one least_frequent char
            has_least = False
            # max_variance_with_least tracks the best variance seen so far for this specific pair
            # that satisfies the "at least one least_frequent" condition.
            max_variance_with_least = 0
            
            # To handle the "at least one least_frequent" constraint, we track the 
            # best variance we could have had *before* the current sequence of least_frequent chars.
            # This allows us to "bridge" over a sequence of least_frequent chars.
            best_prev_variance_without_least = 0

            for char in s:
                if char == most_frequent:
                    current_variance += 1
                elif char == least_frequent:
                    current_variance -= 1
                    # If we encounter a least_frequent, we reset the 'best_prev' 
                    # because we can't use a window that doesn't include this char 
                    # to satisfy the requirement for the *next* window.
                    # Actually, a simpler way:
                    # If we hit a least_frequent, the current window MUST include it.
                    # We track the best variance we had before this least_frequent char.
                    has_least = True
                    # We use a trick: if we hit a least_frequent, we can potentially 
                    # start a new window or extend the old one.
                    # But we must ensure the 'least' is present.
                    # Let's use the standard Kadane approach with a flag.
                    
                # Standard Kadane logic for (most - least)
                # If current_variance becomes too low, we reset.
                # But we can't just reset to 0 if we need to ensure 'least' is present.
                # A better way:
                # current_variance = max(0, current_variance) is standard.
                # To ensure 'least' is present, we track the max variance seen 
                # when 'has_least' was true.
                
            # Re-implementing the logic clearly:
            # We want to maximize (count_most - count_least) subject to count_least > 0.
            # Let's use the 'max_variance_with_least' approach.
            
            current_val = 0
            # max_val_without_least tracks the best (most - least) we've seen 
            # that does NOT currently include a 'least' character in its tail.
            # This is used to "restart" the Kadane sum when it drops below 0.
            max_val_without_least = 0
            # has_least_in_current_window tracks if the current Kadane sum includes a 'least'
            has_least_in_current_window = False
            
            # Resetting for the actual loop
            current_val = 0
            has_least_in_current_window = False
            # We need to track the best variance that includes at least one 'least' char.
            # We can use a state-based Kadane.
            # state 0: haven't seen a 'least' char in current window
            # state 1: have seen at least one 'least' char in current window
            
            # Let's use: 
            # current_sum: the running sum of (most=1, least=-1, other=0)
            # max_sum_with_least: the best sum we've seen that includes at least one 'least'
            # max_sum_without_least: the best sum we've seen that does NOT include a 'least'
            # (This is used to restart the sum)
            
            # Actually, the most robust way for this specific problem:
            # current_sum: standard Kadane sum
            # max_sum_with_least: max(current_sum) where the window contains 'least'
            # To ensure 'least' is in the window, when we encounter 'least', 
            # we can take the best sum seen so far (even if it was 0) and subtract 1.
            
            current_sum = 0
            max_sum_with_least = -float('inf')
            # best_sum_so_far is the max sum we can "attach" to a new 'least' character.
            # It's the max of (0, previous Kadane sums).
            best_sum_so_far = 0 
            
            # We need to be careful: if we encounter 'least', the new sum is 
            # (best_sum_so_far + (-1)). This ensures the 'least' is included.
            # If we encounter 'most', the new sum is (current_sum + 1).
            
            # Let's refine:
            current_sum = 0
            max_sum_with_least = -float('inf')
            # This tracks the best sum we've seen that *could* be extended by a 'least' char.
            # It's essentially the max(0, current_sum) but we need to handle the 
            # "must include least" carefully.
            
            # Correct logic:
            # We want to find max(count_most - count_least) where count_least > 0.
            # Let f(i) = 1 if s[i] == most, -1 if s[i] == least, 0 otherwise.
            # We want max sum of f(i) in a subarray containing at least one -1.
            
            # Let's use two variables:
            # running_sum: standard Kadane sum
            # running_sum_with_least: max sum of a subarray ending at i that contains at least one 'least'
            
            running_sum = 0
            running_sum_with_least = -float('inf')
            
            for char in s:
                if char == most_frequent:
                    running_sum += 1
                    if running_sum_with_least != -float('inf'):
                        running_sum_with_least += 1
                elif char == least_frequent:
                    # If we hit a 'least', the new running_sum_with_least is 
                    # either (running_sum - 1) or (0 - 1) if we start fresh.
                    # But we can only start fresh if we include this 'least'.
                    # The best sum ending here with a 'least' is max(running_sum - 1, -1)
                    # Wait, if we use max(0, running_sum) - 1, it covers both cases.
                    running_sum_with_least = max(0, running_sum) - 1
                    running_sum -= 1
                    # If running_sum drops below 0, we reset it for the next 'most'
                    if running_sum < 0:
                        running_sum = 0
                else:
                    # Other character: doesn't change the sum, but can be part of the window
                    if running_sum_with_least != -float('inf'):
                        running_sum_with_least += 0 # stays same
                    # running_sum stays same
                
                # Note: The 'else' case for 'other' characters is actually:
                # running_sum += 0, running_sum_with_least += 0.
                # But if running_sum was 0, it stays 0.
                
                # However, if running_sum was 0 and we hit an 'other', 
                # we don't want to reset it to 0 if it was already 0.
                # Actually, standard Kadane: if char is 'other', running_sum += 0.
                # If running_sum becomes < 0, reset to 0.
                # But 'other' characters don't make the sum < 0.
                
                # Let's re-verify the 'least' logic:
                # If char == least:
                #    running_sum_with_least = max(running_sum, 0) - 1
                #    running_sum = max(0, running_sum - 1)
                # This is slightly wrong. Let's use the most robust version:
                
            # RE-RE-IMPLEMENTING (Final attempt at logic):
            # We want max subarray sum of [1, -1, 0] with at least one -1.
            # Let dp_with[i] be max sum ending at i with at least one -1.
            # Let dp_without[i] be max sum ending at i with zero -1s.
            
            dp_with = -float('inf')
            dp_without = 0
            
            for char in s:
                if char == most_frequent:
                    dp_with += 1
                    dp_without += 1
                elif char == least_frequent:
                    # To get a 'with' sum, we can take a 'without' sum and add -1,
                    # or take an existing 'with' sum and add -1.
                    dp_with = max(dp_without - 1, dp_with - 1)
                    # A 'without' sum cannot contain a 'least' char.
                    # So if we hit a 'least', the 'without' sum for the next step is 0.
                    dp_without = 0
                else:
                    # Other char: dp_with stays same (if it exists), dp_without stays same.
                    # But if dp_without was 0, it stays 0.
                    # If dp_with was -inf, it stays -inf.
                    # If dp_without was > 0, it stays > 0.
                    # Actually, dp_without is just the count of 'most' since the last 'least'.
                    # If we hit an 'other', dp_without doesn't change.
                    # If we hit a 'most', dp_without increases.
                    # If we hit a 'least', dp_without resets to 0.
                    pass 
                
                # Wait, the 'else' case for 'other' is:
                # dp_with += 0
                # dp_without += 0
                # This is correct.
                
                # But we must handle the case where dp_without becomes negative?
                # No, because dp_without only increments on 'most'.
                # However, if we hit a 'least', dp_without becomes 0.
                # If we hit an 'other', dp_without stays the same.
                # If we hit a 'most', dp_without increases.
                # This is essentially: dp_without = count of 'most' since last 'least' or start.
                
                # Let's refine the loop one last time:
                # (This is the one that actually works)
            
            # Resetting variables for the actual loop
            dp_with = -float('inf')
            dp_without = 0
            for char in s:
                if char == most_frequent:
                    dp_with += 1
                    dp_without += 1
                elif char == least_frequent:
                    dp_with = max(dp_without - 1, dp_with - 1)
                    dp_without = 0
                else:
                    # char is 'other'
                    # dp_with += 0
                    # dp_without += 0
                    pass
                
                if dp_with > max_variance:
                    max_variance = dp_with
                    
    return max_variance

# The logic above is slightly flawed in the 'else' case. 
# Let's provide the clean, correct version.

def solve(s: str) -> int:
    """
    Finds the maximum variance of any substring in the given string.
    """
    n = len(s)
    if n == 0:
        return 0

    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    unique_chars = list(char_counts.keys())
    max_variance = 0

    for most_frequent in unique_chars:
        for least_frequent in unique_chars:
            if most_frequent == least_frequent:
                continue
            if char_counts[least_frequent] == 0:
                continue

            # dp_with: max sum ending at current index that includes at least one least_frequent
            # dp_without: max sum ending at current index that includes zero least_frequent
            dp_with = -float('inf')
            dp_without = 0
            
            for char in s:
                if char == most_frequent:
                    dp_with += 1
                    dp_without += 1
                elif char == least_frequent:
                    # To have a 'with' sum, we either:
                    # 1. Add this 'least' to a previous 'without' sum
                    # 2. Add this 'least' to a previous 'with' sum
                    dp_with = max(dp_without - 1, dp_with - 1)
                    # A 'without' sum cannot include a 'least' char, so it resets
                    dp_without = 0
                else:
                    # 'other' char: dp_with and dp_without don't change their sum
                    # but they still "end" at this index.
                    # dp_with += 0
                    # dp_without += 0
                    pass
                
                # If dp_without becomes negative, it's better to start a new window
                # but a 'without' window can only contain 'most' characters, 
                # so dp_without will never be < 0.
                
                if dp_with > max_variance:
                    max_variance = dp_with
                    
    return max_variance

# Final check on the logic:
# If s = "xyxyy", most='y', least='x'
# 1. char='x': dp_with = max(0-1, -inf-1) = -1, dp_without = 0. max_var = -1 (no, max_var=0)
# 2. char='y': dp_with = -1+1 = 0, dp_without = 0+1 = 1. max_var = 0
# 3. char='x': dp_with = max(1-1, 0-1) = 0, dp_without = 0. max_var = 0
# 4. char='y': dp_with = 0+1 = 1, dp_without = 0+1 = 1. max_var = 1
# 5. char='y': dp_with = 1+1 = 2, dp_without = 1+1 = 2. max_var = 2
# Result 2. Correct.

# If s = "xyx", most='x', least='y'
# 1. char='x': dp_with = -inf, dp_without = 1. max_var = 0
# 2. char