METADATA = {
    "id": 3780,
    "name": "Maximum Sum of Three Numbers Divisible by Three",
    "slug": "maximum-sum-of-three-numbers-divisible-by-three",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of three elements from an array such that the sum is divisible by three.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of exactly three numbers from the input list 
    such that the sum is divisible by 3.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of three numbers divisible by 3. 
        Returns -1 if no such triplet exists.

    Examples:
        >>> solve([3, 3, 3, 3])
        9
        >>> solve([1, 2, 3, 4, 5])
        12
        >>> solve([1, 1, 1])
        3
        >>> solve([1, 2])
        -1
    """
    # We only need to track the top 3 largest numbers for each remainder (0, 1, 2)
    # to ensure we can always pick 3 numbers that satisfy the divisibility rule.
    # Using 3 because we need to pick exactly 3 numbers.
    remainders = {
        0: [],
        1: [],
        2: []
    }

    for num in nums:
        rem = num % 3
        remainders[rem].append(num)
        # Keep only the top 3 largest numbers for each remainder to maintain O(1) space
        remainders[rem].sort(reverse=True)
        if len(remainders[rem]) > 3:
            remainders[rem].pop()

    max_sum = -1

    # Possible combinations of remainders (r1, r2, r3) that sum to a multiple of 3:
    # 1. (0, 0, 0) -> 0+0+0 = 0
    # 2. (1, 1, 1) -> 1+1+1 = 3
    # 3. (2, 2, 2) -> 2+2+2 = 6
    # 4. (0, 1, 2) -> 0+1+2 = 3
    
    combinations = [
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 2),
        (0, 1, 2)
    ]

    for r1, r2, r3 in combinations:
        # Check if we have enough numbers for the chosen remainder pattern
        # We need to handle cases where r1, r2, r3 are the same or different
        temp_lists = []
        
        # We use a frequency map approach to ensure we don't reuse the same index
        # but since we only stored the top 3, we can just check counts.
        needed = {0: 0, 1: 0, 2: 0}
        needed[r1] += 1
        needed[r2] += 1
        needed[r3] += 1

        valid_combination = True
        current_sum = 0
        
        for rem, count in needed.items():
            if len(remainders[rem]) < count:
                valid_combination = False
                break
            # Take the 'count' largest numbers from the stored list for this remainder
            current_sum += sum(remainders[rem][:count])
        
        if valid_combination:
            max_sum = max(max_sum, current_sum)

    return max_sum
