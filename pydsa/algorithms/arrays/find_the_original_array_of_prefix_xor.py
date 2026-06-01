METADATA = {
    "id": 2433,
    "name": "Find The Original Array of Prefix Xor",
    "slug": "find-the-original-array-of-prefix-xor",
    "category": "Array",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reconstruct the original array from its prefix XOR array using the property that elements can be recovered via XORing adjacent prefix values.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Reconstructs the original array from its prefix XOR array.

    The relationship between an array `arr` and its prefix XOR array `nums` is:
    nums[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
    
    From this, we can derive:
    nums[0] = arr[0]
    nums[i] = nums[i-1] ^ arr[i] for i > 0
    
    Rearranging the second equation using XOR properties:
    arr[i] = nums[i] ^ nums[i-1]

    Args:
        nums: A list of integers representing the prefix XOR array.

    Returns:
        A list of integers representing the original array.

    Examples:
        >>> solve([1, 1, 2])
        [1, 0, 2]
        >>> solve([15, 7, 12])
        [15, 8, 11]
    """
    n = len(nums)
    # Initialize the result array with the same size
    original_array = [0] * n
    
    # The first element of the original array is always the first element of the prefix XOR array
    original_array[0] = nums[0]
    
    # Iterate through the prefix XOR array starting from the second element
    for i in range(1, n):
        # Use the property: arr[i] = prefix_xor[i] ^ prefix_xor[i-1]
        # This works because (prefix_xor[i-1] ^ arr[i]) ^ prefix_xor[i-1] = arr[i]
        original_array[i] = nums[i] ^ nums[i - 1]
        
    return original_array
