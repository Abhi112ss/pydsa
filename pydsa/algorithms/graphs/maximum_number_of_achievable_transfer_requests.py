METADATA = {
    "id": 1601,
    "name": "Maximum Number of Achievable Transfer Requests",
    "slug": "maximum-number-of-achievable-transfer-requests",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "graph", "bit_mask", "bit manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of transfer requests that can be satisfied such that each person's net change in money is zero.",
}

def solve(sender_nums: list[int], receiver_nums: list[int], requests: list[list[int]]) -> int:
    """
    Calculates the maximum number of transfer requests that can be satisfied.
    
    A set of requests is valid if for every person, the sum of money sent 
    equals the sum of money received.

    Args:
        sender_nums: A list of integers representing the initial money of each person.
        receiver_nums: A list of integers representing the final money of each person.
        requests: A list of [sender, receiver] pairs representing transfer requests.

    Returns:
        The maximum number of requests that can be satisfied.

    Examples:
        >>> solve([1, 0], [0, 1], [[0, 1]])
        1
        >>> solve([1, 1, 1], [0, 0, 0], [[0, 1], [1, 2], [2, 0]])
        3
    """
    n_people = len(sender_nums)
    n_requests = len(requests)
    
    # Calculate the net change required for each person to reach their target state.
    # net_change[i] = target_money[i] - initial_money[i]
    # However, it is easier to track the balance: 
    # balance[i] = (money received) - (money sent)
    # We want balance[i] to be 0 for all i.
    # Let's use: balance[i] = receiver_nums[i] - sender_nums[i]
    # But wait, the problem asks for the net change to be zero.
    # If we satisfy a subset of requests, for each person:
    # sum(money_received_from_requests) - sum(money_sent_in_requests) == receiver_nums[i] - sender_nums[i]
    # Actually, the problem implies that the requests are the ONLY way money moves.
    # So for each person: (Initial + Received) - Sent = Final
    # Which simplifies to: Received - Sent = Final - Initial
    
    target_balances = [receiver_nums[i] - sender_nums[i] for i in range(n_people)]
    
    max_satisfied = 0

    def backtrack(request_idx: int, current_balances: list[int], count: int) -> None:
        nonlocal max_satisfied
        
        # Base case: all requests considered
        if request_idx == n_requests:
            # Check if all people have the required net balance
            if all(bal == 0 for bal in current_balances):
                # Wait, the target_balances logic above is slightly flawed for the subset approach.
                # Let's redefine: We want to find a subset of requests such that 
                # for every person, the net change from the subset equals (receiver_nums[i] - sender_nums[i]).
                # Actually, the problem states: "the net change in money for each person is zero".
                # This means the subset of requests must result in every person's balance being 0.
                pass
            return

    # Correct approach:
    # We need to find a subset of requests such that for every person i:
    # (Sum of money received in subset) - (Sum of money sent in subset) == 0
    # Wait, the problem says: "the net change in money for each person is zero".
    # This means the requests themselves must balance out.
    # If person A sends to B, A's balance is -1, B's is +1.
    # For the net change to be zero, the sum of all changes must be zero for every person.
    
    # Let's use the net balance approach:
    # For each person, track their current balance based on selected requests.
    # We want current_balance[i] == 0 for all i.
    
    # Pre-calculate the net change required for each person.
    # Actually, the problem implies the requests are the ONLY changes.
    # So we want to pick a subset of requests such that for every person,
    # (number of times they are a receiver) - (number of times they are a sender) == 0
    # Wait, the problem doesn't mention amounts, just the requests.
    # "Each request is [sender, receiver]". This implies 1 unit of money.
    # So for each person: count(as receiver) - count(as sender) == 0.
    
    # Let's re-read: "the net change in money for each person is zero".
    # This means for every person i, the number of times they appear as a receiver 
    # in the chosen subset must equal the number of times they appear as a sender.
    
    # Wait, the problem says: "the net change in money for each person is zero".
    # This is only possible if the subset of requests forms a collection of cycles.
    # Let's use the balance array.
    
    current_balances = [0] * n_people
    
    def backtrack_optimized(idx: int, count: int) -> None:
        nonlocal max_satisfied
        
        # Pruning: if even if we take all remaining requests, we can't beat max_satisfied
        if count + (n_requests - idx) <= max_satisfied:
            return
            
        if idx == n_requests:
            # Check if all balances are zero
            if all(b == 0 for b in current_balances):
                max_satisfied = max(max_satisfied, count)
            return

        # Option 1: Include requests[idx]
        u, v = requests[idx]
        current_balances[u] -= 1
        current_balances[v] += 1
        backtrack_optimized(idx + 1, count + 1)
        # Backtrack
        current_balances[u] += 1
        current_balances[v] -= 1
        
        # Option 2: Exclude requests[idx]
        backtrack_optimized(idx + 1, count)

    # The problem is actually simpler: the sender_nums and receiver_nums are 
    # actually irrelevant if the "net change is zero" refers to the requests themselves.
    # Let's re-read carefully: "the net change in money for each person is zero".
    # This means the sum of all transfers for each person must be 0.
    # This is exactly what I wrote: count(receiver) - count(sender) == 0.
    
    # However, the problem provides sender_nums and receiver_nums. 
    # Let's check if they are used. 
    # "A set of requests is valid if the net change in money for each person is zero."
    # This means the requests themselves must balance out. 
    # The sender_nums and receiver_nums are actually NOT used to determine validity,
    # they are just part of the input to define the people.
    # Wait, if the net change is zero, then the total money in the system remains the same.
    # The sender_nums and receiver_nums are actually just to tell us how many people there are.
    # Let's re-verify. If person 0 sends to person 1, person 0's money changes by -1.
    # For net change to be 0, person 0 must receive 1 from someone else.
    
    backtrack_optimized(0, 0)
    return max_satisfied

# The above logic is slightly inefficient for large N. 
# Let's use Bitmask DP for O(2^N * N) where N is number of requests.
# Since N is up to 14, 2^14 = 16384. 16384 * 14 is very small.

def solve_bitmask(sender_nums: list[int], receiver_nums: list[int], requests: list[list[int]]) -> int:
    """
    Optimal implementation using bitmasking to explore all subsets of requests.
    """
    n_requests = len(requests)
    n_people = len(sender_nums)
    max_satisfied = 0
    
    # Pre-calculate the balance change for each request to avoid repeated work
    # request_deltas[i] = {sender: -1, receiver: +1}
    
    for mask in range(1 << n_requests):
        # Count set bits (number of requests in this subset)
        count = bin(mask).count('1')
        
        # Optimization: if this subset can't beat our current max, skip
        if count <= max_satisfied:
            continue
            
        # Calculate balances for this subset
        balances = [0] * n_people
        for i in range(n_requests):
            if (mask >> i) & 1:
                u, v = requests[i]
                balances[u] -= 1
                balances[v] += 1
        
        # Check if all balances are zero
        is_valid = True
        for b in balances:
            if b != 0:
                is_valid = False
                break
        
        if is_valid:
            max_satisfied = count
            
    return max_satisfied

# Re-implementing the solve function to be the most efficient version.
def solve(sender_nums: list[int], receiver_nums: list[int], requests: list[list[int]]) -> int:
    """
    Finds the maximum number of achievable transfer requests using bitmasking.

    Args:
        sender_nums: Initial money of each person.
        receiver_nums: Final money of each person.
        requests: List of [sender, receiver] pairs.

    Returns:
        Maximum number of requests that can be satisfied.
    """
    n_req = len(requests)
    n_people = len(sender_nums)
    max_count = 0
    
    # Iterate through all 2^n possible subsets of requests
    for mask in range(1 << n_req):
        current_count = 0
        # We use a local balance array for each subset
        balances = [0] * n_people
        
        for i in range(n_req):
            if (mask >> i) & 1:
                current_count += 1
                u, v = requests[i]
                balances[u] -= 1
                balances[v] += 1
        
        # If the subset is valid (all balances zero) and better than max_count
        if current_count > max_count:
            if all(b == 0 for b in balances):
                max_count = current_count
                
    return max_count

# Final check on the problem: "the net change in money for each person is zero"
# This means the sum of money sent by person i must equal the sum of money received by person i.
# Since each request is 1 unit, this is exactly what I implemented.
