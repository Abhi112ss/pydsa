METADATA = {
    "id": 3185,
    "name": "Count Pairs That Form a Complete Day II",
    "slug": "count-pairs-that-form-a-complete-day-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of indices (i, j) such that the sum of the number of complete days in their respective arrays is a prime number.",
}

def solve(days: list[list[int]]) -> int:
    """
    Args:
        days: A list of lists where each sublist represents the status of days in a week.

    Returns:
        The number of pairs (i, j) with i < j such that the sum of complete days is prime.
    """
    def count_complete_days(week: list[int]) -> int:
        count = 0
        for day in week:
            if day == 1:
                count += 1
        return count

    def get_primes(limit: int) -> set[int]:
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for p in range(2, int(limit**0.5) + 1):
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
        return {idx for idx, is_prime in enumerate(primes) if is_prime}

    complete_days_counts = []
    for week in days:
        complete_days_counts.append(count_complete_days(week))

    max_possible_sum = 14
    prime_set = get_primes(max_possible_sum)

    frequency_map = {}
    for count in complete_days_counts:
        frequency_map[count] = frequency_map.get(count, 0) + 1

    total_pairs = 0
    unique_counts = list(frequency_map.keys())

    for i in range(len(unique_counts)):
        count_a = unique_counts[i]
        freq_a = frequency_map[count_a]
        
        for j in range(i, len(unique_counts)):
            count_b = unique_counts[j]
            freq_b = frequency_map[count_b]
            
            if (count_a + count_b) in prime_set:
                if i == j:
                    total_pairs += (freq_a * (freq_a - 1)) // 2
                else:
                    total_pairs += freq_a * freq_b

    return total_pairs