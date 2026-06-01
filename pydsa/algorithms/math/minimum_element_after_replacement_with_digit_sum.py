METADATA = {
    "id": 3300,
    "name": "Minimum Element After Replacement With Digit Sum",
    "slug": "minimum-element-after-replacement-with-digit-sum",
    "category": "Greedy",
    "aliases": [],
    "tags": ["math", "greedy", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(k * n log n)",
    "space_complexity": "O(n)",
    "description": "Replace the largest element in an array with its digit sum k times and return the minimum element.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Repeatedly replaces the largest element in the array with its digit sum k times.

    Args:
        nums: A list of integers.
        k: The number of replacement operations to perform.

    Returns:
        The minimum element in the array after k operations.

    Examples:
        >>> solve([10, 20, 30], 1)
        10
        >>> solve([10, 20, 30], 2)
        10
        >>> solve([99, 99, 99], 1)
        18
    """
    def get_digit_sum(n: int) -> int:
        """Calculates the sum of the digits of a given integer."""
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    # Use a max-heap to efficiently retrieve and replace the largest element.
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap.
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    for _ in range(k):
        # Pop the largest element (remembering to negate it back to positive)
        largest = -heapq.heappop(max_heap)
        
        # Calculate the digit sum of the largest element
        digit_sum = get_digit_sum(largest)
        
        # Push the digit sum back into the heap as a negative value
        heapq.heappush(max_heap, -digit_sum)

    # After k operations, the minimum element is the smallest value in the heap.
    # Since we stored negative values, the minimum element is the maximum of the negated values.
    # However, we need the minimum of the actual numbers, which is -max(max_heap).
    # Wait, the minimum element in the original sense is the smallest number in the array.
    # In our max_heap (containing negative numbers), the smallest original number 
    # is the one with the largest absolute value among the negatives? No.
    # Example: nums=[10, 20], heap=[-20, -10]. Min element is 10. 
    # In heap, -10 is the largest value. So min(nums) = -max(max_heap).
    
    # Let's find the actual minimum by looking at all elements in the heap.
    return min(-x for x in max_heap)
