METADATA = {
    "id": 347,
    "name": "Top K Frequent Elements",
    "slug": "top-k-frequent-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["heap", "hash_map", "bucket_sort"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums and an integer k, return the k most frequent elements.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements in an integer array using bucket sort.

    Args:
        nums: A list of integers.
        k: The number of most frequent elements to return.

    Returns:
        A list containing the k most frequent elements.

    Examples:
        >>> solve([1, 1, 1, 2, 2, 3], 2)
        [1, 2]
        >>> solve([1], 1)
        [1]
    """
    # Step 1: Count the frequency of each number using a hash map
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Use bucket sort where the index represents the frequency.
    # The maximum possible frequency is len(nums).
    # buckets[i] will store a list of numbers that appear exactly 'i' times.
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequency_map.items():
        buckets[freq].append(num)

    # Step 3: Iterate through the buckets from highest frequency to lowest
    # and collect elements until we reach k elements.
    result: list[int] = []
    for frequency in range(len(buckets) - 1, 0, -1):
        for num in buckets[frequency]:
            result.append(num)
            if len(result) == k:
                return result

    return result
