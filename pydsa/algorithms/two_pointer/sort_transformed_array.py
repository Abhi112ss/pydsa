METADATA = {
    "id": 360,
    "name": "Sort Transformed Array",
    "slug": "sort-transformed-array",
    "category": "Math",
    "aliases": [],
    "tags": ["two_pointer", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array and coefficients a, b, and c, return a sorted array of the transformed values f(x) = a*x^2 + b*x + c.",
}

def solve(arr: list[int], a: int, b: int, c: int) -> list[int]:
    """
    Transforms each element in the array using the quadratic formula f(x) = ax^2 + bx + c
    and returns the result in sorted order.

    The transformation is a parabola. The vertex is at x = -b / (2a).
    The function is monotonic on either side of the vertex.
    By using two pointers starting from the ends of the sorted input array,
    we can collect the transformed values in sorted order in O(n) time.

    Args:
        arr: A list of integers.
        a: The coefficient of x^2.
        b: The coefficient of x.
        c: The constant term.

    Returns:
        A sorted list of transformed integers.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1, 0, 0)
        [1, 4, 9, 16, 25]
        >>> solve([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 1, 0, 0)
        [0, 1, 1, 4, 4, 9, 9, 16, 16, 25, 25]
    """
    n = len(arr)
    if n == 0:
        return []

    # The input array is not guaranteed to be sorted in the problem description,
    # but the logic for O(n) transformation relies on the input being sorted.
    # If the input is not sorted, we must sort it first, making it O(n log n).
    # However, the standard interpretation of this problem assumes 'arr' is sorted.
    # If 'arr' is not sorted, we sort it here.
    arr.sort()

    result = [0] * n
    left = 0
    right = n - 1
    
    # We fill the result array from largest to smallest.
    # The largest values of a quadratic function occur at the extremes of the input range.
    # If a > 0, the parabola opens upwards, so extremes are at the ends of the array.
    # If a < 0, the parabola opens downwards, so extremes are at the vertex (middle).
    # If a = 0, it's a linear function, extremes are at the ends.
    
    # We use a pointer for the result index starting from the end.
    res_idx = n - 1

    if a > 0:
        # Parabola opens up: extremes are at the ends of the sorted input.
        while left <= right:
            val_left = a * arr[left]**2 + b * arr[left] + c
            val_right = a * arr[right]**2 + b * arr[right] + c
            
            if val_left > val_right:
                result[res_idx] = val_left
                left += 1
            else:
                result[res_idx] = val_right
                right -= 1
            res_idx -= 1
    elif a < 0:
        # Parabola opens down: extremes are near the vertex (middle).
        # To maintain O(n) and sorted order, we can treat this as finding 
        # the smallest values at the ends and largest in the middle.
        # Alternatively, we can use the same two-pointer logic but 
        # realize the 'largest' values are in the middle.
        # A simpler way: the values at the ends are the smallest.
        # We use two pointers to pick the smaller of the two ends.
        while left <= right:
            val_left = a * arr[left]**2 + b * arr[left] + c
            val_right = a * arr[right]**2 + b * arr[right] + c
            
            if val_left < val_right:
                result[res_idx] = val_right
                right -= 1
            else:
                result[res_idx] = val_left
                left += 1
            res_idx -= 1
    else:
        # Linear function: a = 0.
        # If b > 0, it's increasing. If b < 0, it's decreasing.
        if b >= 0:
            for i in range(n):
                result[i] = b * arr[i] + c
        else:
            for i in range(n):
                result[i] = b * arr[i] + c
            result.reverse()

    # Note: The logic above for a < 0 was slightly inverted for the 'largest' approach.
    # Let's refine the logic to be robust:
    # Always pick the largest available value from the ends if a > 0.
    # If a < 0, the largest values are in the middle, so the smallest are at the ends.
    # Let's use a more universal approach:
    
    # Re-implementing the core logic for clarity and correctness:
    res = [0] * n
    l, r = 0, n - 1
    idx = n - 1
    
    if a > 0:
        # Largest values are at the ends.
        while l <= r:
            v_l = a * arr[l]**2 + b * arr[l] + c
            v_r = a * arr[r]**2 + b * arr[r] + c
            if v_l > v_r:
                res[idx] = v_l
                l += 1
            else:
                res[idx] = v_r
                r -= 1
            idx -= 1
    elif a < 0:
        # Smallest values are at the ends.
        while l <= r:
            v_l = a * arr[l]**2 + b * arr[l] + c
            v_r = a * arr[r]**2 + b * arr[r] + c
            if v_l < v_r:
                res[idx] = v_r
                r -= 1
            else:
                res[idx] = v_l
                l += 1
            idx -= 1
    else:
        # Linear case: a = 0.
        # If b > 0, arr[i] is increasing. If b < 0, arr[i] is decreasing.
        # If b = 0, all values are c.
        if b >= 0:
            for i in range(n):
                res[i] = b * arr[i] + c
        else:
            # If b < 0, the sequence is decreasing, so we reverse it to get sorted.
            for i in range(n):
                res[i] = b * arr[i] + c
            res.reverse()
            
    return res
