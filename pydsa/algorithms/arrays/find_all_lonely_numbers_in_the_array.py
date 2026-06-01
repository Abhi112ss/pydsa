METADATA = {
    "id": 2150,
    "name": "Find All Lonely Numbers in the Array",
    "slug": "find-all-lonely-numbers-in-the-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all numbers in an array that appear exactly once and have no neighbors with a value of x-1 or x+1.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds all 'lonely' numbers in the input array.
    
    A number is considered lonely if it appears exactly once in the array 
    and neither (number - 1) nor (number + 1) is present in the array.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers containing all the lonely numbers found.

    Examples:
        >>> solve([10, 6, 5, 8])
        [10, 8]
        >>> solve([1, 2, 3, 4])
        []
        >>> solve([1, 1, 1])
        []
    """
    # Step 1: Count the frequency of each number using a hash map
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    lonely_numbers: list[int] = []

    # Step 2: Iterate through the unique numbers to check the loneliness criteria
    for num, count in counts.items():
        # A number must appear exactly once
        if count == 1:
            # Check if neighbors (num - 1) or (num + 1) exist in the frequency map
            if (num - 1) not in counts and (num + 1) not in counts:
                lonely_numbers.append(num)

    return lonely_numbers
