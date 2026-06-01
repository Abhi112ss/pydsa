METADATA = {
    "id": 1279,
    "name": "Traffic Light Controlled Intersection",
    "slug": "traffic_light_controlled_intersection",
    "category": "simulation",
    "aliases": [],
    "tags": ["simulation", "logic"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Simulate cars passing through an intersection controlled by a traffic light.",
}

from collections import deque
from typing import List

def solve(cars: List[int]) -> List[int]:
    """Simulate the traffic light controlled intersection.

    Args:
        cars: List where cars[i] is the direction of the i‑th car arriving at time i.
              Directions 0 and 1 correspond to north‑south (green group 0),
              directions 2 and 3 correspond to east‑west (green group 1).

    Returns:
        A list `answer` where answer[i] is the time at which the i‑th car passes the intersection.

    Examples:
        >>> solve([0, 2, 1, 3])
        [0, 1, 2, 3]
        >>> solve([2, 2, 0, 1, 3])
        [0, 1, 2, 3, 4]
    """
    n: int = len(cars)
    answer: List[int] = [-1] * n

    # Queues for cars waiting in each green group (0: north‑south, 1: east‑west)
    waiting_queues: List[deque[int]] = [deque(), deque()]

    current_time: int = 0          # simulation clock
    next_arrival: int = 0          # index of the next car to arrive
    green_group: int = 0           # 0 means north‑south is green, 1 means east‑west is green

    while next_arrival < n or waiting_queues[0] or waiting_queues[1]:
        # Add all cars that arrive at the current time to their respective queues
        while next_arrival < n and next_arrival <= current_time:
            direction: int = cars[next_arrival]
            group: int = direction // 2          # 0 for north‑south, 1 for east‑west
            waiting_queues[group].append(next_arrival)
            next_arrival += 1

        if waiting_queues[green_group]:
            # A car can go through on the current green direction
            car_index: int = waiting_queues[green_group].popleft()
            answer[car_index] = current_time
            current_time += 1
        elif waiting_queues[1 - green_group]:
            # No car in current green direction, switch the light to the opposite group
            green_group = 1 - green_group
            car_index = waiting_queues[green_group].popleft()
            answer[car_index] = current_time
            current_time += 1
        else:
            # No cars waiting; advance time to the next arrival
            current_time += 1

    return answer