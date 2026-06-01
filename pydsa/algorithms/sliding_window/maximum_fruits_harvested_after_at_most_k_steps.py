METADATA = {
    "id": 2106,
    "name": "Maximum Fruits Harvested After at Most K Steps",
    "slug": "maximum-fruits-harvested-after-at-most-k-steps",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of fruits that can be harvested by moving at most k steps starting from position 0.",
}

def solve(fruits: list[list[int]], start_pos: int, k: int) -> int:
    """
    Calculates the maximum number of fruits that can be harvested within k steps.

    The strategy uses a sliding window approach. For any window [left, right], 
    the minimum steps required to cover all fruits in that window starting from 
    start_pos is:
    1. If the window is entirely to the right of start_pos: right - start_pos
    2. If the window is entirely to the left of start_pos: start_pos - left
    3. If the window straddles start_pos: min(abs(left - start_pos), abs(right - start_pos)) 
       + (right - left)
       Which simplifies to: (right - left) + min(abs(start_pos - left), abs(start_pos - right))

    Args:
        fruits: A list of [position, amount] pairs.
        start_pos: The initial starting position.
        k: The maximum number of steps allowed.

    Returns:
        The maximum total fruit amount possible.

    Examples:
        >>> solve([[2, 8], [5, 6], [8, 6]], 5, 4)
        14
        >>> solve([[9, 2], [6, 3], [4, 1]], 4, 4)
        4
    """
    n = len(fruits)
    max_fruits = 0
    current_window_sum = 0
    left = 0

    # Iterate through the fruits using 'right' as the end of the sliding window
    for right in range(n):
        current_window_sum += fruits[right][1]

        # Calculate the minimum steps needed to cover the current window [left, right]
        # We must visit both fruits[left][0] and fruits[right][0] starting from start_pos
        while left <= right:
            left_pos = fruits[left][0]
            right_pos = fruits[right][0]
            
            # Case 1: Window is entirely to the right of start_pos
            if left_pos >= start_pos:
                steps_needed = right_pos - start_pos
            # Case 2: Window is entirely to the left of start_pos
            elif right_pos <= start_pos:
                steps_needed = start_pos - left_pos
            # Case 3: Window straddles start_pos
            else:
                # We go to the closer end first, then turn back to the further end
                dist_to_left = start_pos - left_pos
                dist_to_right = right_pos - start_pos
                steps_needed = min(dist_to_left, dist_to_right) + (right_pos - left_pos)

            # If steps exceed k, shrink the window from the left
            if steps_needed > k:
                current_window_sum -= fruits[left][1]
                left += 1
            else:
                break

        max_fruits = max(max_fruits, current_window_sum)

    return max_fruits
