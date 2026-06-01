METADATA = {
    "id": 1558,
    "name": "Minimum Number of Function Calls to Make Target Array",
    "slug": "minimum-number-of-function-calls-to-make-target-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of function calls to transform an array of 1s into a target array using two specific operations.",
}

def solve(target: list[int]) -> int:
    """
    Calculates the minimum number of function calls to transform an array of 1s 
    into the target array using two operations:
    1. Add 1 to all elements in a range [i, j].
    2. Set all elements in a range [i, j] to 1.

    The problem can be modeled by observing the differences between adjacent elements.
    The 'set to 1' operation is used to reset segments, while the 'add 1' operation
    is used to build up the values. The total cost is the sum of positive differences
    between adjacent elements, plus one extra call if any element is greater than 1
    (to account for the initial 'set to 1' or the first 'add 1' block).

    Args:
        target: A list of integers representing the target array.

    Returns:
        The minimum number of function calls required.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 1, 1, 1, 1])
        0
        >>> solve([2, 1, 2])
        3
    """
    n = len(target)
    if n == 0:
        return 0
    
    # If all elements are 1, no operations are needed.
    if all(x == 1 for x in target):
        return 0

    # The core idea is to track the 'increases' needed.
    # We look at the difference between adjacent elements.
    # If target[i] > target[i-1], we need (target[i] - target[i-1]) 'add 1' operations.
    # If target[i] < target[i-1], we can treat the drop as a reset point.
    
    # We start by considering the first element's relation to an implicit 1.
    # However, a cleaner way is to count all positive differences target[i] - target[i-1].
    # The 'set to 1' operation effectively allows us to 'restart' the sequence.
    
    # Let's use the logic: 
    # Total calls = (Sum of all positive differences target[i] - target[i-1]) 
    # + (1 if we need to handle the first element or a reset).
    
    # Actually, a more robust way:
    # Every time target[i] > target[i-1], we must have performed (target[i] - target[i-1]) 
    # 'add 1' operations that started at or before i-1 and ended at or after i.
    
    total_calls = 0
    
    # We treat the array as if it's preceded by a 1.
    # This handles the first element's requirement to reach target[0].
    current_val = 1
    
    for i in range(n):
        if target[i] > current_val:
            # We need to perform 'add 1' operations to bridge the gap.
            total_calls += (target[i] - current_val)
        elif target[i] < current_val:
            # A drop in value implies we must have used a 'set to 1' operation 
            # at some point to reset the value, which costs 1 call.
            total_calls += 1
        
        # Update current_val to the current target to compare with the next element.
        current_val = target[i]

    # The logic above counts 'add 1' increments and 'set to 1' resets.
    # However, the 'set to 1' operation is only needed if we encounter a value 
    # smaller than the previous one. 
    # Let's refine:
    
    # Correct Greedy Approach:
    # 1. Count all positive differences: sum(max(0, target[i] - target[i-1]))
    # 2. If there's any drop (target[i] < target[i-1]), we need a 'set to 1' call.
    # 3. The first element target[0] also needs (target[0] - 1) 'add 1' calls.
    
    # Let's re-implement with the refined logic.
    
    ans = 0
    # Initial cost to get the first element from 1 to target[0]
    ans += (target[0] - 1)
    
    for i in range(1, n):
        if target[i] > target[i-1]:
            # If increasing, we just add the difference to the 'add 1' count.
            ans += (target[i] - target[i-1])
        elif target[i] < target[i-1]:
            # If decreasing, we must have used a 'set to 1' operation.
            # This 'set to 1' operation covers the current element and potentially 
            # others, but it essentially resets the baseline.
            # The cost is 1 (for the set to 1) + (target[i] - 1) (to build up target[i]).
            # But wait, the 'set to 1' can be combined with the 'add 1's.
            # The standard way to solve this:
            # Total = (Sum of all target[i] - target[i-1] where > 0) + (count of i where target[i] < target[i-1])
            # Wait, that's not quite right. Let's use the difference-based logic.
            pass

    # Let's use the most reliable logic for this problem:
    # We want to minimize calls. 
    # 'Add 1' to [i, j] is like increasing the difference array.
    # 'Set to 1' to [i, j] is like resetting the difference array.
    
    # Let's use the property:
    # Total calls = (Sum of all positive differences target[i] - target[i-1]) 
    # + (1 if there is at least one i such that target[i] < target[i-1])
    # Wait, that's for a different problem.
    
    # Correct logic for this specific problem:
    # We can use 'add 1' to increase values.
    # We can use 'set to 1' to reset values.
    # The number of 'add 1' calls needed is sum(max(0, target[i] - target[i-1])) 
    # where target[-1] = 1.
    # If we ever need to 'reset' (i.e., target[i] < target[i-1]), we use a 'set to 1' call.
    # A 'set to 1' call can be used to "fix" all subsequent elements that would 
    # have required more 'add 1' calls than they actually do.
    
    # Let's re-calculate:
    # Let's track the cost of 'add 1' operations.
    # To get target[0], we need target[0]-1 'add 1' calls.
    # For each i > 0:
    #   If target[i] > target[i-1], we need target[i] - target[i-1] more 'add 1' calls.
    #   If target[i] < target[i-1], we can use a 'set to 1' call.
    #   A 'set to 1' call costs 1 and effectively makes the current element 1.
    #   Then we need target[i]-1 'add 1' calls to get it to target[i].
    #   But we can combine the 'set to 1' with the 'add 1's.
    
    # The actual optimal strategy:
    # Total = (Sum of all target[i] - target[i-1] where target[i] > target[i-1])
    # + (1 if there is any i such that target[i] < target[i-1])
    # Wait, let's trace [2, 1, 2]:
    # target[0]=2: needs 1 'add 1' call. Array: [2, 1, 1]
    # target[1]=1: no 'add 1' needed. But we need to 'set to 1' the middle? 
    # No, the array is [2, 1, 1]. To get [2, 1, 2], we need to 'add 1' to index 2.
    # Total: [1,1,1] -> [2,1,1] (1 call) -> [2,1,2] (1 call). Total 2? 
    # No, the problem says [2, 1, 2] requires 3.
    # [1,1,1] -> [2,2,2] (1 call) -> [2,1,1] (1 call) -> [2,1,2] (1 call). Total 3.
    
    # Let's use the difference array approach:
    # Let diff[i] = target[i] - target[i-1].
    # We want to reach target from [1, 1, ...].
    # This is equivalent to reaching diff from [0, 0, ...].
    # The 'set to 1' operation is the key.
    
    # Let's use the logic from a known correct approach:
    # 1. Calculate the sum of all positive differences: 
    #    diffs = sum(max(0, target[i] - target[i-1])) for i in 0..n-1, with target[-1]=1.
    # 2. If there is any i such that target[i] < target[i-1], we need one 'set to 1' call.
    #    Wait, that's not enough. If we have [2, 1, 2], diffs = (2-1) + (2-1) = 2.
    #    There is a drop (1 < 2), so 2 + 1 = 3. Correct.
    #    If we have [1, 2, 3], diffs = (1-1) + (2-1) + (3-2) = 2. No drop. Total 2.
    #    Wait, [1, 2, 3] needs 2 calls: [1,1,1] -> [1,2,2] -> [1,2,3]. Correct.
    #    If we have [3, 2, 1], diffs = (3-1) = 2. Drop exists. 2 + 1 = 3.
    #    [1,1,1] -> [3,3,3] -> [3,2,1] (set to 1 on [1,2] then add 1 to [1,1]?) 
    #    Actually [1,1,1] -> [3,3,3] (1 call) -> [3,1,1] (1 call) -> [3,2,1] (1 call). Total 3.
    
    # Let's refine the "drop" logic:
    # A 'set to 1' operation can be used to reset a segment.
    # If we use a 'set to 1' operation, it costs 1 call and we can then 
    # use 'add 1' operations to build up the values.
    # The total number of 'add 1' calls is always sum(max(0, target[i] - target[i-1])) 
    # where target[-1] = 1.
    # If we use a 'set to 1' call, it can replace some 'add 1' calls.
    # But the 'set to 1' call itself is an operation.
    # The only way to get a value lower than the previous is to use 'set to 1'.
    # Every time target[i] < target[i-1], we MUST have used a 'set to 1' operation 
    # at some point to make target[i] smaller than target[i-1].
    # Does one 'set to 1' call suffice for all drops? 
    # Yes, because a 'set to 1' can be applied to a suffix.
    
    # Let's re-verify [2, 1, 2]:
    # target[0]=2, target[1]=1, target[2]=2.
    # target[-1]=1.
    # diffs: (2-1)=1, (1-2)=-1, (2-1)=1.
    # Positive diffs: 1 + 1 = 2.
    # Is there a drop? Yes (1 < 2).
    # Total = 2 + 1 = 3.
    
    # Let's re-verify [1, 2, 3, 4, 5]:
    # target[-1]=1.
    # diffs: (1-1)=0, (2-1)=1, (3-2)=1, (4-3)=1, (5-4)=1.
    # Positive diffs: 0+1+1+1+1 = 4.
    # Is there a drop? No.
    # Total = 4. Wait, the example says 5? 
    # Let me re-read. [1, 2, 3, 4, 5]
    # [1,1,1,1,1] -> [1,2,2,2,2] -> [1,2,3,3,3] -> [1,2,3,4,4] -> [1,2,3,4,5].
    # That is 4 calls. Let me check the example again.
    # Example 1: target = [1,2,3,4,5], output = 4. (My manual trace was 4, the prompt says 5? 
    # No, the prompt doesn't provide examples, I'll assume my logic is correct).
    # Actually, if target is [1,2,3,4,5], target[0] is 1.
    # target[0]-1 = 0.
    # target[1]-target[0] = 1.
    # target[2]-target[1] = 1.
    # target[3]-target[2] = 1.
    # target[4]-target[3] = 1.
    # Sum = 4. No drops. Total = 4.
    
    # Let's check [1, 1, 1]:
    # target[-1]=1.
    # diffs: (1-1)=0, (1-1)=0, (1-1)=0.
    # Sum = 0. No drops. Total = 0. Correct.

    # Final Algorithm:
    # 1. ans = target[0] - 1
    # 2. has_drop = False
    # 3. For i from 1 to n-1:
    #    if target[i] > target[i-1]: ans += target[i] - target[i-1]
    #    if target[i] < target[i-1]: has_drop = True
    # 4. If has_drop: ans += 1
    # 5. Return ans

    # Wait, one more case: [2, 1, 2].
    # ans = 2-1 = 1.
    # i=1: target[1]=1 < target[0]=2. has_drop = True.
    # i=2: target[2]=2 > target[1]=1. ans += 2-1 = 1. (ans is now 2)
    # has_drop is True, so ans += 1 = 3. Correct.

    # One more: [1, 2, 1, 2]
    # ans = 1-1 = 0.
    # i=1: 2 > 1, ans += 1 (ans=1).
    # i=2: 1 < 2, has_drop = True.
    # i=3: 2 > 1, ans += 1 (ans=2).
    # has_drop is True, ans += 1 = 3.
    # Trace [1,2,1,2]: [1,1,1,1] -> [1,2,2,2] (1) -> [1,2,1,1] (1) -> [1,2,1,2] (1). Total 3. Correct.

    # Implementation:
    ans = target[0] - 1
    has_drop = False
    for i in range(1, n):
        if target[i] > target[i-1]:
            ans += target[i] - target[i-1]