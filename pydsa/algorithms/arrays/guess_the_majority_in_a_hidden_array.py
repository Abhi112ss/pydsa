METADATA = {
    "id": 1538,
    "name": "Guess the Majority in a Hidden Array",
    "slug": "guess-the-majority-in-a-hidden-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_val - min_val) * log n)",
    "space_complexity": "O(1)",
    "description": "Find the majority element in a hidden array using binary search on the value range.",
}

class HiddenArray:
    """
    A mock class representing the hidden array interface provided by the problem.
    In a real LeetCode environment, this is provided by the judge.
    """
    def __init__(self, data: list[int]):
        self.data = data

    def get(self, index: int) -> int:
        return self.data[index]

    def length(self) -> int:
        return len(self.data)

def solve(hidden_array: HiddenArray) -> int:
    """
    Finds the majority element in a hidden array using binary search on the value range.
    
    The majority element is defined as an element that appears more than n/2 times.
    Since the array is not sorted, we cannot binary search on indices. Instead, 
    we binary search on the possible range of values [min_val, max_val].

    Args:
        hidden_array: An object providing `get(index)` and `length()` methods.

    Returns:
        The majority element in the hidden array.

    Examples:
        >>> arr = HiddenArray([3, 2, 3])
        >>> solve(arr)
        3
        >>> arr2 = HiddenArray([1, 1, 2, 2, 2])
        >>> solve(arr2)
        2
    """
    n = hidden_array.length()
    
    # In a real LeetCode problem, the range of values is usually given or 
    # can be inferred. Assuming standard 32-bit integer range or 
    # finding min/max via a single pass if allowed. 
    # For this implementation, we assume the range is [0, 10^9] or similar.
    # If the range is not provided, we'd need to find min/max first.
    
    low = -10**9  # Adjust based on problem constraints
    high = 10**9
    
    # To make this robust for any range, we first find the actual min/max
    # if the problem constraints allow O(n) to find the range.
    # However, the prompt asks for O(log n) which implies the range is fixed
    # or we are binary searching the value space.
    
    # Let's refine the range based on the problem's typical constraints.
    # If we don't know the range, we can use the first element to start.
    # But for a general solution, we assume a standard integer range.
    
    # Note: The prompt asks for O(log n) time. Strictly speaking, 
    # counting occurrences takes O(n), so the total time is O(n * log(Range)).
    # The "O(log n)" in the prompt likely refers to the search steps 
    # if the array were sorted, but for a hidden unsorted array, 
    # we must iterate through the array to count.
    
    # Finding the actual range to ensure correctness
    # This part is O(n)
    min_val = hidden_array.get(0)
    max_val = hidden_array.get(0)
    for i in range(1, n):
        val = hidden_array.get(i)
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    ans = min_val
    left, right = min_val, max_val

    while left <= right:
        mid = (left + right) // 2
        
        # Count how many elements are <= mid
        count_le = 0
        for i in range(n):
            if hidden_array.get(i) <= mid:
                count_le += 1
        
        # If count of elements <= mid is greater than n/2, 
        # the majority element must be in the range [left, mid]
        # or it is the majority element itself.
        # Actually, the logic for majority element via value binary search:
        # If count(elements <= mid) > n/2, the majority element is <= mid.
        # Otherwise, it is > mid.
        
        if count_le > n // 2:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    # The binary search finds the smallest value 'v' such that 
    # count(elements <= v) > n/2. This 'v' is the majority element.
    return ans
