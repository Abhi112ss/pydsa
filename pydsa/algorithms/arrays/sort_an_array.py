METADATA = {
    "id": 912,
    "name": "Sort an Array",
    "slug": "sort-an-array",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "merge_sort", "heap_sort", "quick_sort"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an array of integers, sort the array in ascending order.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Sorts an array of integers in ascending order using the Merge Sort algorithm.

    Merge Sort is chosen because it guarantees O(n log n) time complexity, 
    which is necessary to pass the constraints of this problem where 
    Quick Sort might hit O(n^2) worst-case scenarios.

    Args:
        nums: A list of integers to be sorted.

    Returns:
        A new list containing the integers in ascending order.

    Examples:
        >>> solve([5, 2, 3, 1])
        [1, 2, 3, 5]
        >>> solve([-1, 5, 0, 10, -10])
        [-10, -1, 0, 5, 10]
    """
    if not nums:
        return []

    def merge_sort_recursive(arr: list[int]) -> list[int]:
        # Base case: a list of size 0 or 1 is already sorted
        if len(arr) <= 1:
            return arr

        # Divide: Find the midpoint and split the array into two halves
        midpoint = len(arr) // 2
        left_half = merge_sort_recursive(arr[:midpoint])
        right_half = merge_sort_recursive(arr[midpoint:])

        # Conquer: Merge the two sorted halves back together
        return merge(left_half, right_half)

    def merge(left: list[int], right: list[int]) -> list[int]:
        sorted_list = []
        left_index = 0
        right_index = 0

        # Compare elements from both halves and append the smaller one
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        # Append any remaining elements from the left or right lists
        # One of these will be empty, the other will contain the remaining sorted elements
        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])

        return sorted_list

    return merge_sort_recursive(nums)
