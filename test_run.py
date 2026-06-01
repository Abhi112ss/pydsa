from pydsa import solve, search, info

# Test 1: Fuzzy Natural Language Search
print("--- Test 1: Natural Language ---")
try:
    result = solve("find pair that sums to target", [2, 7, 11, 15], 9)
    print(f"Algorithm Selected: {result.problem}")
    print(f"Answer: {result.answer}")
    print(f"Complexity: Time {result.time_complexity}, Space {result.space_complexity}")
except Exception as e:
    print(f"Failed: {e}")

# Test 2: Browse Problems
print("\n--- Test 2: Semantic Search ---")
matches = search("sliding window", limit=3)
for p in matches:
    print(f"- {p.id}: {p.name} ({p.difficulty})")