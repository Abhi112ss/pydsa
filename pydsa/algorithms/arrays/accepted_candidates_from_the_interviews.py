METADATA = {
    "id": 2041,
    "name": "Accepted Candidates From the Interviews",
    "slug": "accepted_candidates_from_the_interviews",
    "category": "array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count candidates whose acceptance ratio is strictly greater than all previous candidates.",
}


def solve(accepted: list[int], interviews: list[int]) -> int:
    """Count the number of candidates whose acceptance ratio is strictly greater than any
    candidate before them.

    Args:
        accepted: List of integers where accepted[i] is the number of accepted offers for
            candidate i.
        interviews: List of integers where interviews[i] is the total number of interviews
            conducted for candidate i. Both lists have the same length.

    Returns:
        The count of candidates whose accepted[i] / interviews[i] ratio is strictly larger
        than the maximum ratio observed among all previous candidates.

    Examples:
        >>> solve([2, 1, 3, 4], [2, 2, 4, 5])
        3
        >>> solve([1, 2, 3], [1, 2, 3])
        1
    """
    if not accepted or not interviews or len(accepted) != len(interviews):
        return 0

    count_of_good_candidates = 0
    max_accepted = 0
    max_interviews = 1  # avoid division by zero; ratio = 0 initially

    for idx in range(len(accepted)):
        current_accepted = accepted[idx]
        current_interviews = interviews[idx]

        # Compare fractions without floating point: a/b > c/d  <=> a*d > c*b
        if current_accepted * max_interviews > max_accepted * current_interviews:
            count_of_good_candidates += 1
            max_accepted = current_accepted
            max_interviews = current_interviews

    return count_of_good_candidates