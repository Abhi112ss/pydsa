METADATA = {
    "id": 997,
    "name": "Find the Town Judge",
    "slug": "find_the_town_judge",
    "category": "graph",
    "aliases": [],
    "tags": ["graph", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n+e)",
    "space_complexity": "O(n)",
    "description": "Identify the town judge based on trust relationships."
}

import sys
from typing import List

def solve() -> None:
    """Read input, compute and print the town judge.

    Input format:
        n
        m
        a1 b1
        a2 b2
        ...
        am bm

    where `n` is the number of people labeled from 1 to n,
    `m` is the number of trust relationships,
    and each pair `ai bi` means person `ai` trusts person `bi`.

    Returns:
        Prints the label of the town judge if one exists; otherwise prints -1.

    Example:
        Input:
            3
            2
            1 3
            2 3
        Output:
            3
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Parse n and m
    n = int(data[0])
    if len(data) == 1:
        # No trust information provided
        print(1 if n == 1 else -1)
        return

    m = int(data[1])
    trust: List[List[int]] = []
    idx = 2
    for _ in range(m):
        if idx + 1 >= len(data):
            break
        a = int(data[idx])
        b = int(data[idx + 1])
        trust.append([a, b])
        idx += 2

    # Edge case: single person with no trust relationships
    if n == 1 and not trust:
        print(1)
        return

    # net_score[i] = in-degree - out-degree for person i
    net_score = [0] * (n + 1)

    for a, b in trust:
        net_score[a] -= 1   # a trusts someone, so out-degree increases
        net_score[b] += 1   # b is trusted, so in-degree increases

    # The judge must be trusted by everyone else (n-1) and trust nobody
    judge = -1
    for person in range(1, n + 1):
        if net_score[person] == n - 1:
            judge = person
            break

    print(judge)