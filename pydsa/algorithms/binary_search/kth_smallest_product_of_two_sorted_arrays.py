METADATA = {
    "id": 2040,
    "name": "Kth Smallest Product of Two Sorted Arrays",
    "slug": "kth-smallest-product-of-two-sorted-arrays",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(log(max_prod) * (N + M))",
    "space_complexity": "O(1)",
    "description": "Find the kth smallest product of two elements from two sorted arrays containing both positive and negative integers.",
}

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    """
    Finds the kth smallest product of two elements from two sorted arrays.

    Args:
        nums1: A sorted list of integers.
        nums2: A sorted list of integers.
        k: The rank of the product to find (1-indexed).

    Returns:
        The kth smallest product.

    Examples:
        >>> solve([-4, -2, 0, 3], [-1, 4], 1)
        -16
        >>> solve([-4, -2, 0, 3], [-1, 4], 2)
        -8
    """

    def count_less_equal(target: int) -> int:
        """Counts how many products are <= target using two pointers/binary search."""
        count = 0
        for x in nums1:
            if x > 0:
                # For positive x, x * y <= target => y <= target / x
                # Since nums2 is sorted, we find the rightmost index where nums2[i] <= target / x
                # Using binary search for efficiency within the loop
                low, high = 0, len(nums2) - 1
                pos = -1
                while low <= high:
                    mid = (low + high) // 2
                    if x * nums2[mid] <= target:
                        pos = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                count += (pos + 1)
            elif x < 0:
                # For negative x, x * y <= target => y >= target / x
                # Since nums2 is sorted, we find the leftmost index where nums2[i] >= target / x
                low, high = 0, len(nums2) - 1
                pos = len(nums2)
                while low <= high:
                    mid = (low + high) // 2
                    if x * nums2[mid] <= target:
                        pos = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                count += (len(nums2) - pos)
            else:
                # If x is 0, 0 <= target is either always true or always false
                if target >= 0:
                    count += len(nums2)
        return count

    # The range of possible products is between the minimum and maximum possible products
    # Min product can be from (large positive * large negative) or (large negative * large positive)
    # Max product can be from (large positive * large positive) or (large negative * large negative)
    # To be safe, we use the extreme bounds of the product space.
    left = -10**10
    right = 10**10
    
    # Refine bounds based on actual array values to speed up search
    # However, 10^10 is safe for the constraints (10^5 * 10^5)
    
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        # Check if the number of products <= mid is at least k
        if count_less_equal(mid) >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans
