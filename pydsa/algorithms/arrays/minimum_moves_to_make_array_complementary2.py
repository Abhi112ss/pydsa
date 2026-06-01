METADATA = {
    "id": 1674,
    "name": "Minimum Moves to Make Array Complementary",
    "slug": "minimum-moves-to-make-array-complementary",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array complementary to a target array using a difference array approach.",
}

def solve(nums: list[int], limit: int) -> int:
    n = len(nums)

    diff = [0] * (2 * limit + 2)

    for i in range(n // 2):
        a = nums[i]
        b = nums[n - 1 - i]

        low = min(a, b)
        high = max(a, b)
        s = a + b

        diff[2] += 2

        diff[low + 1] -= 1
        diff[s] -= 1

        diff[s + 1] += 1
        diff[high + limit + 1] += 1

    ans = float("inf")
    curr = 0

    for target in range(2, 2 * limit + 1):
        curr += diff[target]
        ans = min(ans, curr)

    return ans