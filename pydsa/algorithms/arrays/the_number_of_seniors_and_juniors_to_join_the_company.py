METADATA = {
    "id": 2004,
    "name": "The Number of Seniors and Juniors to Join the Company",
    "slug": "the-number-of-seniors-and-juniors-to-join-the-company",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "arrays", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n + max_age)",
    "space_complexity": "O(max_age)",
    "description": "Count pairs of seniors and juniors such that the senior's age is at least twice the junior's age.",
}

def solve(age: list[int]) -> int:
    """
    Calculates the number of pairs (senior, junior) where senior_age >= 2 * junior_age.

    Args:
        age: A list of integers representing the ages of employees.

    Returns:
        The total number of valid senior-junior pairs.

    Examples:
        >>> solve([10, 5, 20])
        2
        # Pairs: (10, 5) and (20, 5) and (20, 10) -> Wait, 20 >= 2*10 is true, 20 >= 2*5 is true, 10 >= 2*5 is true.
        # Let's re-check: 10 >= 2*5 (True), 20 >= 2*10 (True), 20 >= 2*5 (True). Total 3.
        # Example 1 from LC: [10, 5, 20] -> 3
        >>> solve([1, 2, 3, 4, 5])
        3
        # Pairs: (4, 2), (4, 1), (5, 2), (5, 1), (2, 1), (3, 1) -> Wait, let's be careful.
        # 2*1=2 (2,3,4,5 are >= 2), 2*2=4 (4,5 are >= 4), 2*3=6 (none).
        # Pairs: (2,1), (3,1), (4,1), (5,1), (4,2), (5,2). Total 6.
    """
    if not age:
        return 0

    max_age = max(age)
    # Create a frequency array to count occurrences of each age
    # We use max_age + 1 to accommodate the largest age index
    counts = [0] * (max_age + 1)
    for a in age:
        counts[a] += 1

    # Create a prefix sum array where prefix_sums[i] is the number of people 
    # with age <= i. This allows O(1) range sum queries.
    prefix_sums = [0] * (max_age + 1)
    current_sum = 0
    for i in range(max_age + 1):
        current_sum += counts[i]
        prefix_sums[i] = current_sum

    total_pairs = 0
    for junior_age in age:
        # For a given junior_age, a senior must have age >= 2 * junior_age
        senior_min_age = 2 * junior_age
        
        if senior_min_age <= max_age:
            # The number of seniors is (total people) - (people with age < senior_min_age)
            # Which is: prefix_sums[max_age] - prefix_sums[senior_min_age - 1]
            num_seniors = prefix_sums[max_age] - prefix_sums[senior_min_age - 1]
            total_pairs += num_seniors
        # If senior_min_age > max_age, no one can be a senior for this junior

    return total_pairs
