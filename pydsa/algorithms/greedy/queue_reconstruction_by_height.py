METADATA = {
    "id": 406,
    "name": "Queue Reconstruction by Height",
    "slug": "queue-reconstruction-by-height",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Reconstruct a queue given people's heights and the number of people in front of them who are taller or equal in height.",
}

def solve(people: list[list[int]]) -> list[list[int]]:
    """
    Reconstructs the queue based on the given height and count constraints.

    The strategy is to sort the people in descending order of height. 
    For people with the same height, sort them in ascending order of their 'k' value.
    Then, iterate through the sorted list and insert each person into the 
    result list at the index specified by their 'k' value.

    Args:
        people: A list of lists where each sub-list contains [h, k].
                h is the height and k is the number of people in front 
                with height >= h.

    Returns:
        A list of lists representing the reconstructed queue.

    Examples:
        >>> solve([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        >>> solve([[1,0]])
        [[1, 0]]
    """
    # Sort people: 
    # 1. Primary key: height (h) descending (-x[0])
    # 2. Secondary key: count (k) ascending (x[1])
    # This ensures that when we process a person, all people already in the 
    # result list are taller or equal in height.
    people.sort(key=lambda x: (-x[0], x[1]))

    reconstructed_queue: list[list[int]] = []

    for person in people:
        # The 'k' value tells us exactly how many people taller or equal 
        # to the current person should be in front. Since we process 
        # from tallest to shortest, the current 'k' is the exact index 
        # where this person should be inserted to maintain the property.
        reconstructed_queue.insert(person[1], person)

    return reconstructed_queue
