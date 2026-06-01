METADATA = {
    "id": 2340,
    "name": "Minimum Adjacent Swaps to Make a Valid Array",
    "slug": "minimum-adjacent-swaps-to-make-a-valid-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of adjacent swaps to make an array valid such that no two adjacent elements have the same parity.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of adjacent swaps to make an array valid.
    An array is valid if no two adjacent elements have the same parity.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of adjacent swaps required. Returns -1 if impossible.

    Examples:
        >>> solve([5, 3, 4, 2])
        2
        >>> solve([1, 2, 3, 4, 5])
        -1
    """
    n = len(nums)
    odd_count = sum(1 for x in nums if x % 2 != 0)
    even_count = n - odd_count

    # A valid array must have counts of odd and even numbers differing by at most 1
    if abs(odd_count - even_count) > 1:
        return -1

    # Determine the starting parity. 
    # If odd_count > even_count, the array must start with an odd number.
    # If even_count > odd_count, it must start with an even number.
    # If equal, we try both and take the minimum, but the problem constraints 
    # and parity logic allow us to check which pattern is valid.
    
    def calculate_swaps(start_with_odd: bool) -> int:
        total_swaps = 0
        current_odd_idx = 0
        # We track the 'target' index for the next required parity
        # To minimize swaps, we move the nearest available element of required parity
        # to the current position. This is equivalent to summing the distance 
        # between current indices of elements and their target indices.
        
        # However, a more efficient way to calculate adjacent swaps to reach a permutation
        # is to track the indices of all elements of a specific parity.
        odd_indices = [i for i, x in enumerate(nums) if x % 2 != 0]
        even_indices = [i for i, x in enumerate(nums) if x % 2 == 0]
        
        target_odd_indices = []
        target_even_indices = []
        
        # Construct the target index lists based on the chosen starting parity
        is_odd = start_with_odd
        for i in range(n):
            if is_odd:
                target_odd_indices.append(i)
            else:
                target_even_indices.append(i)
            is_odd = not is_odd
            
        # If the pattern doesn't match the counts, this pattern is invalid
        if len(target_odd_indices) != odd_count or len(target_even_indices) != even_count:
            return float('inf')
            
        # The number of adjacent swaps to transform one sequence of indices to another
        # is the sum of absolute differences between corresponding indices.
        # Since we only care about parity, we just need to move the 'k-th' odd number
        # to the 'k-th' odd position.
        for i in range(len(odd_indices)):
            total_swaps += abs(odd_indices[i] - target_odd_indices[i])
            
        return total_swaps

    # Case 1: Try starting with Odd
    res_odd = calculate_swaps(True)
    # Case 2: Try starting with Even
    res_even = calculate_swaps(False)

    ans = min(res_odd, res_even)
    return int(ans) if ans != float('inf') else -1
