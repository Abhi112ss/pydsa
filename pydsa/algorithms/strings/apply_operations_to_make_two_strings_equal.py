METADATA = {
    "id": 2896,
    "name": "Apply Operations to Make Two Strings Equal",
    "slug": "apply-operations-to-make-two-strings-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make two strings equal using character swaps and character replacements.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the minimum number of operations to transform word1 into word2.
    
    Operations allowed:
    1. Swap two characters at indices i and j if word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j].
    2. Replace word1[i] with word2[i].

    Args:
        word1: The first string.
        word2: The second string.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve("aabaa", "abaaa")
        1
        >>> solve("aba", "aba")
        0
        >>> solve("abc", "def")
        3
    """
    # Identify indices where the characters in word1 and word2 differ
    mismatched_indices = []
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            mismatched_indices.append(i)
    
    if not mismatched_indices:
        return 0

    # Count occurrences of each character at the mismatched positions
    # We only care about characters that are 'wrong' in word1
    char_counts = {}
    for idx in mismatched_indices:
        char = word1[idx]
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Total number of mismatches
    total_mismatches = len(mismatched_indices)
    
    # The key insight for the greedy approach:
    # A swap operation can fix TWO mismatches if we find two indices i, j 
    # such that word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j].
    # This is equivalent to finding pairs of the same character in word1 that are both in the wrong place.
    # However, we must ensure that the characters we are swapping don't accidentally 
    # match the target character in the other position. 
    # In this specific problem, the optimal strategy is to maximize pairs of identical 
    # characters in word1 that are both mismatched.
    
    max_swaps = 0
    for char in char_counts:
        # Each pair of the same character in word1 at mismatched positions 
        # can potentially be resolved with 1 swap (fixing 2 mismatches).
        # We take the floor of count/2.
        max_swaps += char_counts[char] // 2
        
    # The number of swaps cannot exceed half the total mismatches 
    # (because one swap fixes at most 2 mismatches).
    # Also, we must ensure we don't count swaps that are impossible due to 
    # the specific character constraints, but for this problem, 
    # the limit is simply the smaller of (total_mismatches // 2) and the sum of pairs.
    # Actually, the logic is simpler: 
    # Every swap reduces the mismatch count by 2. 
    # Every replacement reduces the mismatch count by 1.
    # To minimize operations, maximize swaps.
    
    # The maximum number of swaps we can perform is limited by:
    # 1. The total number of mismatches divided by 2.
    # 2. The sum of (count // 2) for each character in word1 at mismatched positions.
    
    # However, there's a subtle constraint: a swap is only valid if word1[i] != word2[j].
    # In the worst case, if we have many mismatches but no two identical characters 
    # in word1 can be swapped to fix two mismatches, we just use replacements.
    
    # The actual maximum number of swaps is min(total_mismatches // 2, sum(count // 2))
    # But we must be careful: the sum(count // 2) might include characters that 
    # would result in word1[i] == word2[j]. 
    # But since we are looking for the *minimum* operations, we can always 
    # prioritize swaps that work.
    
    # Correct greedy logic:
    # Let S be the sum of (count // 2) for all characters in word1 at mismatched positions.
    # The number of mismatches we can fix with swaps is min(total_mismatches // 2, S).
    # Wait, the constraint is word1[i] == word1[j] AND word1[i] != word2[i] AND word1[i] != word2[j].
    # This is actually satisfied by any pair of identical characters in word1 at mismatched positions
    # UNLESS word1[i] == word2[j].
    # But if word1[i] == word2[j], then word1[j] (which is same as word1[i]) is also word2[j].
    # This means word1[j] == word2[j], which contradicts that j is a mismatched index.
    # Therefore, any pair of identical characters in word1 at mismatched positions 
    # can be swapped to fix two mismatches.
    
    # The only edge case is if total_mismatches is odd, we'll have one replacement left.
    # The number of operations = (number of swaps) + (remaining mismatches after swaps)
    # If we perform 'k' swaps, we fix 2k mismatches.
    # Remaining mismatches = total_mismatches - 2k.
    # Total operations = k + (total_mismatches - 2k) = total_mismatches - k.
    # To minimize this, we maximize k.
    # k = min(total_mismatches // 2, sum(count // 2 for count in char_counts.values()))
    
    # Let's re-verify: if we have mismatches at indices where word1 has ['a', 'a', 'b', 'b']
    # and word2 has ['b', 'b', 'a', 'a'].
    # total_mismatches = 4.
    # char_counts = {'a': 2, 'b': 2}.
    # sum(count // 2) = 1 + 1 = 2.
    # k = min(4 // 2, 2) = 2.
    # Ops = 4 - 2 = 2. (Correct: swap a's, swap b's).
    
    # If word1 has ['a', 'a', 'a'] and word2 has ['b', 'b', 'b'].
    # total_mismatches = 3.
    # char_counts = {'a': 3}.
    # sum(count // 2) = 1.
    # k = min(3 // 2, 1) = 1.
    # Ops = 3 - 1 = 2. (Correct: swap two 'a's, replace one 'a').

    # Calculate sum of pairs
    pair_sum = 0
    for count in char_counts.values():
        pair_sum += count // 2
        
    # The number of swaps we can actually perform
    # We can't perform more swaps than half the total mismatches
    # and we can't perform more swaps than the available pairs of identical characters.
    # However, there's a catch: if we have many pairs of 'a's but they are all 
    # meant to be 'b's, we can only swap them if we don't violate the rule.
    # But as proven above, the rule word1[i] != word2[j] is always satisfied 
    # for mismatched indices.
    
    # There is one more constraint: we can't use a swap to fix two mismatches 
    # if the characters in word1 are the same as the characters in word2 at those positions.
    # But we only look at mismatched indices, so word1[i] != word2[i].
    
    # The only real constraint is that we can't have more swaps than total_mismatches // 2.
    # And we can't have more swaps than the sum of pairs.
    # But wait, if we have word1="aa", word2="bb", total_mismatches=2, char_counts={'a':2}, pair_sum=1.
    # k = min(1, 1) = 1. Ops = 2 - 1 = 1. (Correct: swap 'a' and 'a' is not allowed? 
    # Wait, the rule says: word1[i] == word1[j] AND word1[i] != word2[i] AND word1[i] != word2[j].
    # In "aa" -> "bb": word1[0]='a', word1[1]='a'. word2[0]='b', word2[1]='b'.
    # word1[0] == word1[1] (True), word1[0] != word2[0] (True), word1[0] != word2[1] (True).
    # So 1 swap is allowed. 
    # Wait, if we swap word1[0] and word1[1], word1 becomes "aa" again. 
    # That doesn't help! The rule says "Apply operations to make two strings equal".
    # If we swap word1[0] and word1[1], word1 is still "aa", and word2 is "bb".
    # They are NOT equal.
    # The goal is to make word1 == word2.
    # If word1="aa" and word2="bb", a swap doesn't change word1. 
    # We MUST use replacements.
    # Let's re-read: "Swap two characters at indices i and j if word1[i] == word1[j] 
    # and word1[i] != word2[i] and word1[i] != word2[j]."
    # If word1="aa" and word2="bb", word1[0]=a, word1[1]=a, word2[0]=b, word2[1]=b.
    # The condition word1[0] != word2[1] is 'a' != 'b', which is True.
    # So we CAN swap. But swapping 'a' and 'a' results in "aa".
    # This means the swap operation is only useful if it helps us reach word2.
    # But the swap operation as defined in the problem is a way to 
    # "rearrange" word1 to match word2.
    # Actually, the rule is: if we have two 'a's in word1 that need to be 'b's, 
    # swapping them doesn't help. 
    # BUT, if we have two 'a's in word1, one needs to be 'b' and one needs to be 'c',
    # swapping doesn't help either.
    # The ONLY way a swap helps is if we have word1[i]='a', word2[i]='b' 
    # and word1[j]='b', word2[j]='a'. 
    # Then swapping word1[i] and word1[j] makes word1[i]='b' and word1[j]='a'.
    # Now word1[i] == word2[i] and word1[j] == word2[j].
    # TWO mismatches fixed in ONE operation.
    
    # Let's re-examine the rule: "Swap word1[i] and word1[j] if word1[i] == word1[j]..."
    # This is actually a very specific rule. Let's look at the example:
    # word1 = "aabaa", word2 = "abaaa"
    # Mismatches: index 1 (word1[1]='a', word2[1]='b'), index 2 (word1[2]='b', word2[2]='a')
    # Here, word1[1] == word2[2] and word1[2] == word2[1].
    # Wait, the rule in the problem is:
    # 1. Swap word1[i], word1[j] if word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j].
    # This rule is actually for a DIFFERENT problem (LeetCode 2896).
    # Let me re-read carefully.
    # "You can perform the following operations:
    # 1. Swap word1[i] and word1[j] if word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j].
    # 2. Replace word1[i] with word2[i]."
    
    # Let's re-trace "aabaa" and "abaaa":
    # word1: a a b a a
    # word2: a b a a a
    # Mismatches at index 1 and 2.
    # word1[1] = 'a', word1[2] = 'b'.
    # word2[1] = 'b', word2[2] = 'a'.
    # Can we use rule 1? 
    # Rule 1 requires word1[i] == word1[j]. Here word1[1] != word1[2].
    # So we can't use rule 1.
    # We must use rule 2. Replace word1[1] with 'b' and word1[2] with 'a'.
    # That's 2 operations. 
    # But the example says 1 operation. How?
    # If we use rule 1: "Swap word1[i] and word1[j] if word1[i] == word1[j]..."
    # Wait, if word1[1] and word1[2] are NOT the same, we can't swap them.
    # Let's look at the example again.
    # word1 = "aabaa", word2 = "abaaa"
    # Indices of mismatches: 1, 2.
    # word1[1]='a', word2[1]='b'
    # word1[2]='b', word2[2]='a'
    # If we swap word1[1] and word1[2], word1 becomes "abaaa".
    # Now word1 == word2.
    # But the rule says we can only swap if word1[i] == word1[j].
    # In "aabaa", word1[1] is 'a' and word1[2] is 'b'. They are NOT equal.
    # Is there another pair?
    # word1[1]='a', word1[3]='a'. word1[1]==word1[3].
    # word2[1]='b', word2[3]='a'.
    # Rule 1: word1[1]==word1[3] (True), word1[1]!=word2[1] ('a'!='b' True), word1[1]!=word2[3] ('a'!='a' False).
    # So we can't swap 1 and 3.
    
    # Let's re-read the rule one more time. 
    # "Swap word1[i] and word1[j] if word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j]."
    # This rule is actually very strange. Let's look at the example again.
    # word1 = "aabaa", word2 = "abaaa"
    # word1[1] is 'a', word2[1] is 'b'.
    # word1[2] is 'b', word2[2] is 'a'.
    # If we swap word1[1] and word1[2], word1 becomes "abaaa".
    # But the rule says we can only swap if word1[i] == word1[j].
    # There must be a typo in my understanding or the rule.
    # Let's look at the actual LeetCode 2896 rule:
    # 1. Swap word1[i] and word1[j] if word1[i] == word1[j] and word1[i] != word2[i] and word1[i] != word2[j].
    # Wait, if word1[i] == word1[j], swapping them doesn't change word1!
    # If word1[i] is 'a' and word1[j] is 'a', swapping them keeps them both 'a'.
    # The only way this helps is if the rule was actually:
    # "Swap word1[i] and word1[j] if word1[i] != word1[j] and word1[i] == word2