METADATA = {
    "id": 3049,
    "name": "Earliest Second to Mark Indices II",
    "slug": "earliest-second-to-mark-indices-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sliding_window", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum time required such that there exists a subarray of length k where the sum of elements at even indices and odd indices satisfies a specific difference condition.",
}

def solve(nums: list[int], k: int, diff: int) -> int:
    """
    Args:
        nums: A list of integers.
        k: The required length of the subarray.
        diff: The required minimum difference between the sum of even-indexed elements and odd-indexed elements.

    Returns:
        The earliest second to mark the indices, or -1 if impossible.
    """
    n = len(nums)

    def check(time: int) -> bool:
        even_sum = 0
        odd_sum = 0
        
        current_nums = []
        for i in range(n):
            val = nums[i]
            if time < val:
                current_nums.append(0)
            else:
                current_nums.append(val)

        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)

        for i in range(n):
            prefix_even[i + 1] = prefix_even[i]
            prefix_odd[i + 1] = prefix_odd[i]
            if i % 2 == 0:
                prefix_even[i + 1] += current_nums[i]
            else:
                prefix_odd[i + 1] += current_nums[i]

        for i in range(k, n + 1):
            current_even = prefix_even[i] - prefix_even[i - k]
            current_odd = prefix_odd[i] - prefix_odd[i - k]
            if abs(current_even - current_odd) >= diff:
                return True
        return False

    low = 1
    high = 10**9
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        
        even_sum_window = 0
        odd_sum_window = 0
        
        current_even_prefix = [0] * (n + 1)
        current_odd_prefix = [0] * (n + 1)
        
        for i in range(n):
            val = nums[i] if nums[i] <= mid else 0
            current_even_prefix[i + 1] = current_even_prefix[i]
            current_odd_prefix[i + 1] = current_odd_prefix[i]
            if i % 2 == 0:
                current_even_prefix[i + 1] += val
            else:
                current_odd_prefix[i + 1] += val
        
        possible = False
        for i in range(k, n + 1):
            e = current_even_prefix[i] - current_even_prefix[i - k]
            o = current_odd_prefix[i] - current_odd_prefix[i - k]
            if abs(e - o) >= diff:
                possible = True
                break
        
        if possible:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans