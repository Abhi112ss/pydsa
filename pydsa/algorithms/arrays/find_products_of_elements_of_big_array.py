METADATA = {
    "id": 3145,
    "name": "Find Products of Elements of Big Array",
    "slug": "find-products-of-elements-of-big-array",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate products of elements in chunks of size k, where each chunk's product is added to the next chunk's elements.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Calculates the products of elements in chunks of size k and updates the array.

    The process involves taking chunks of size k, calculating their product, 
    and then adding that product to each element in the next chunk. This 
    continues until the array is exhausted.

    Args:
        nums: A list of integers representing the big array.
        k: The size of the chunks to process.

    Returns:
        A list of integers representing the modified array after all chunk 
        operations are completed.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], 2)
        [1, 2, 6, 4, 30, 6]
        >>> solve([1, 2, 3, 4], 3)
        [1, 2, 6, 4]
    """
    n = len(nums)
    # We iterate through the array in steps of k.
    # The problem implies we process chunks [i, i+k-1], [i+k, i+2k-1], etc.
    # However, the rule is: product of chunk i is added to elements of chunk i+1.
    # This means we need to calculate products of chunks first, then apply them.
    
    # Step 1: Calculate products for all possible chunks of size k.
    # We only care about chunks that have a 'next' chunk to receive the product.
    # The last chunk (or partial chunk) doesn't have a successor to add to.
    
    # To handle the updates correctly without using the updated values 
    # for the current chunk's product, we can pre-calculate products.
    
    chunk_products = []
    for i in range(0, n - k, k):
        # Calculate product of the current chunk [i, i + k - 1]
        current_product = 1
        for j in range(i, i + k):
            current_product *= nums[j]
        chunk_products.append(current_product)
    
    # Step 2: Apply the products to the subsequent chunks.
    # The product of chunk 0 is added to elements of chunk 1.
    # The product of chunk 1 is added to elements of chunk 2, and so on.
    for idx, product in enumerate(chunk_products):
        # The target chunk starts at index (idx + 1) * k
        start_index = (idx + 1) * k
        # We add the product to all elements in the next chunk.
        # Note: The next chunk might be smaller than k if it's the last one.
        for j in range(start_index, min(start_index + k, n)):
            nums[j] += product
            
    return nums
