METADATA = {
    "id": 1969,
    "name": "Minimum Non-Zero Product of the Array Elements",
    "slug": "minimum-non-zero-product-of-the-array-elements",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum non-zero product of an array after performing at most one operation to change an element to zero.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum non-zero product of the array elements after 
    at most one operation (changing one element to zero).

    To minimize the non-zero product, we should identify the largest 
    non-zero element and effectively "remove" it from the product calculation.

    Args:
        nums: A list of integers.

    Returns:
        The minimum non-zero product as an integer.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        24
        >>> solve([1, 0, 2, 3, 4, 5])
        24
        >>> solve([0, 0, 0])
        0
    """
    MOD = 10**9 + 7
    
    # Filter out zeros to focus on the non-zero product
    non_zero_elements = [x for x in nums if x != 0]
    
    # If there are no non-zero elements, the product is 0
    if not non_zero_elements:
        return 0
    
    # If there is only one non-zero element, changing it to zero 
    # results in a non-zero product of 0 (if we consider the product of an empty set)
    # However, the problem implies we want the minimum product of the remaining elements.
    # If we turn the only non-zero element to zero, the product of non-zeros is 0.
    # But the problem asks for the minimum non-zero product. 
    # If we have [5], turning 5 to 0 makes the product of non-zeros 0.
    # Wait, the problem asks for the minimum non-zero product. 
    # If we turn the only non-zero element to 0, the product of non-zeros is 0.
    # But 0 is not a non-zero product. 
    # Actually, the rule is: if we turn an element to 0, we calculate the product of 
    # the remaining elements that are NOT zero.
    
    # Find the maximum non-zero element to exclude it
    max_val = 0
    total_product = 1
    
    for val in non_zero_elements:
        if val > max_val:
            max_val = val
        total_product = (total_product * val) % MOD
        
    # To get the product without the max element, we can't simply divide 
    # because of the modulo and potential zeros. 
    # Since we only need to exclude ONE element, we can just re-calculate 
    # or use the property that we want to exclude the largest.
    
    # Re-calculating the product excluding the max_val is safer for modulo arithmetic
    # and handles the case where multiple elements have the same max value.
    
    # We need to find the product of all non-zero elements except one instance of max_val.
    # Because we want the MINIMUM product, we must remove the largest element.
    
    # Let's find the index of the first occurrence of max_val to exclude it.
    max_val_index = -1
    for i, val in enumerate(nums):
        if val == max_val:
            max_val_index = i
            break
            
    min_product = 1
    found_max = False
    
    for i, val in enumerate(nums):
        if val != 0 and i != max_val_index:
            min_product = (min_product * val) % MOD
            
    # If the array was all zeros or turning the max to zero leaves no non-zeros
    # The problem implies we want the product of the remaining non-zero elements.
    # If all elements are zero, product is 0.
    # If we turn the only non-zero element to zero, the product of non-zeros is 0.
    # But the question asks for the minimum non-zero product.
    # If the result of the product is 0, we return 0.
    
    # Check if there were any non-zero elements left after excluding max_val
    # If non_zero_elements had only 1 element, the loop above results in min_product = 1.
    # But if we exclude the only non-zero element, the product of "remaining non-zeros" is 0.
    if len(non_zero_elements) == 1:
        return 0

    return min_product % MOD
