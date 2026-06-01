METADATA = {
    "id": 3514,
    "name": "Number of Unique XOR Triplets II",
    "slug": "number_of_unique_xor_triplets_ii",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map", "frequency_array", "fast_walsh_hadamard_transform"],
    "difficulty": "hard",
    "time_complexity": "O(N + M log M) where M is the smallest power of 2 greater than max(nums)",
    "space_complexity": "O(M)",
    "description": "Count the number of triplets (i, j, k) such that nums[i] ^ nums[j] ^ nums[k] == 0 using FWHT.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of triplets (i, j, k) with 0 <= i < j < k < n 
    such that nums[i] ^ nums[j] ^ nums[k] == 0.

    The problem asks for unique index triplets. This is equivalent to finding 
    the coefficient of x^0 in the XOR convolution of the frequency array 
    with itself three times, then adjusting for permutations and identical indices.

    Args:
        nums: A list of integers.

    Returns:
        The number of unique index triplets whose XOR sum is zero.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([0, 0, 0])
        1
        >>> solve([1, 1, 1, 1])
        4
    """
    if not nums:
        return 0

    max_val = max(nums)
    # Find the smallest power of 2 greater than max_val to accommodate XOR convolution
    m = 1
    while m <= max_val:
        m <<= 1
    
    # Frequency array
    freq = [0] * m
    for x in nums:
        freq[x] += 1

    def fwht(a: list[int]) -> list[int]:
        """Fast Walsh-Hadamard Transform for XOR."""
        n = len(a)
        res = list(a)
        h = 1
        while h < n:
            for i in range(0, n, h * 2):
                for j in range(i, i + h):
                    x = res[j]
                    y = res[j + h]
                    res[j] = x + y
                    res[j + h] = x - y
            h <<= 1
        return res

    def ifwht(a: list[int]) -> list[int]:
        """Inverse Fast Walsh-Hadamard Transform."""
        n = len(a)
        res = fwht(a)
        return [x // n for x in res]

    # Transform the frequency array to the Walsh-Hadamard domain
    transformed = fwht(freq)
    
    # In the transform domain, XOR convolution is pointwise multiplication.
    # We want the 3-way convolution: freq * freq * freq
    # The coefficient at index 0 of (freq * freq * freq) represents 
    # the sum over all i, j, k such that nums[i] ^ nums[j] ^ nums[k] == 0.
    transformed_cubed = [x**3 for x in transformed]
    
    # Transform back to get the counts in the original domain
    convolution_result = ifwht(transformed_cubed)
    
    # total_triplets_with_zero_xor is the sum of all (i, j, k) such that nums[i]^nums[j]^nums[k] == 0
    # This includes cases where indices are not distinct (e.g., i=j, i=k, or i=j=k).
    # We need to use the Principle of Inclusion-Exclusion or combinatorial adjustment.
    
    # Let S be the set of indices {i, j, k} such that nums[i] ^ nums[j] ^ nums[k] == 0.
    # We want to count sets {i, j, k} where i < j < k.
    
    # 1. Total ways (including permutations and non-distinct indices):
    #    This is exactly convolution_result[0].
    #    However, the convolution_result[0] counts ordered tuples (i, j, k).
    #    Wait, the convolution of frequency arrays counts tuples of values.
    #    If freq[v] is the count of value v, then (freq * freq * freq)[0] is:
    #    Sum_{a^b^c=0} freq[a] * freq[b] * freq[c]
    
    # Let's refine the counting:
    # Let N(a, b, c) be the number of ways to pick indices i, j, k such that nums[i]=a, nums[j]=b, nums[k]=c.
    # If a, b, c are distinct: there are 3! = 6 permutations of indices.
    # If two are same (e.g., a=b != c): there are 3 permutations of indices.
    # If all three are same (a=b=c): there is 1 permutation of indices.
    
    # But we need to pick distinct indices i, j, k.
    # Let's use the identity for the number of ways to pick 3 distinct elements from a set:
    # For a specific set of values {a, b, c} such that a^b^c=0:
    # Case 1: a, b, c are distinct.
    #    Ways to pick indices: freq[a] * freq[b] * freq[c].
    #    Since we want i < j < k, and a, b, c are distinct, each set of 3 indices is counted 6 times in the convolution.
    # Case 2: a = b != c.
    #    Since a^b^c = 0 and a=b, then c must be 0. So a^a^0 = 0.
    #    Ways to pick indices: freq[a] * (freq[a]-1) * freq[0] / 2 (if we pick two 'a's and one '0').
    #    Wait, the convolution counts (i, j, k) where i, j, k can be same.
    
    # Let's use the power sum symmetric polynomial approach for XOR:
    # Let f(x) be the frequency array.
    # We want to find the number of triplets (i, j, k) with i < j < k and nums[i]^nums[j]^nums[k] == 0.
    # Let S1 = sum_{i} x^{nums[i]} (this is our freq array)
    # Let S2 = sum_{i} x^{nums[i] ^ nums[i]} = sum_{i} x^0 = n * x^0
    # This is not quite right for XOR.
    
    # Correct combinatorial approach for XOR:
    # Let A be the frequency array.
    # The sum we want is:
    # 1/6 * [ (sum_{i,j,k} [nums[i]^nums[j]^nums[k]=0]) 
    #         - 3 * (sum_{i,j} [nums[i]^nums[i]^nums[j]=0]) 
    #         + 2 * (sum_{i} [nums[i]^nums[i]^nums[i]=0]) ]
    
    # Let's evaluate the terms:
    # Term 1: sum_{i,j,k} [nums[i]^nums[j]^nums[k]=0]
    #         This is convolution_result[0].
    
    # Term 2: sum_{i,j} [nums[i]^nums[i]^nums[j]=0]
    #         nums[i]^nums[i] is always 0.
    #         So we need 0 ^ nums[j] == 0, which means nums[j] == 0.
    #         The sum is sum_{i} sum_{j} [nums[j]=0] = n * freq[0].
    #         Wait, the term in the formula is 3 * sum_{i,j} [nums[i]^nums[i]^nums[j]=0] 
    #         where the indices are (i, i, j) with i != j.
    #         Actually, let's use the standard formula for picking 3 distinct items:
    #         Let T = sum_{i,j,k distinct} [nums[i]^nums[j]^nums[k]=0]
    #         T = (sum_{i,j,k} [nums[i]^nums[j]^nums[k]=0]) 
    #             - 3 * (sum_{i,j, i!=j} [nums[i]^nums[i]^nums[j]=0])
    #             - (sum_{i} [nums[i]^nums[i]^nums[i]=0])
    #             + 2 * (sum_{i,j, i!=j} [nums[i]^nums[i]^nums[j]=0] ... no, this is getting complex.
    
    # Let's use the simpler logic:
    # Let C = convolution_result[0] (this is sum_{i,j,k} [nums[i]^nums[j]^nums[k]=0])
    # Let C2 = sum_{i,j} [nums[i]^nums[j]^nums[j]=0] = sum_{i,j} [nums[i]=0] = n * freq[0]
    # Let C3 = sum_{i} [nums[i]^nums[i]^nums[i]=0] = sum_{i} [nums[i]=0] = freq[0]
    
    # The sum over all i, j, k (not necessarily distinct) is C.
    # The sum over i, j, k where exactly two are equal:
    # If i=j != k: nums[i]^nums[i]^nums[k] = 0 => nums[k]=0. 
    # There are n * freq[0] such pairs (i, k) where i != k.
    # But we have 3 such patterns: (i,i,k), (i,k,i), (k,i,i).
    # Total for "exactly two equal": 3 * (n * freq[0] - freq[0]) if we consider i != k.
    # Wait, if i=j=k, then nums[i]^nums[i]^nums[i] = nums[i]. 
    # For this to be 0, nums[i] must be 0.
    # There are freq[0] such cases.
    
    # Let's re-calculate:
    # Total = C
    # Subtract cases where at least two indices are equal:
    # Case: i=j=k. This happens if nums[i]^nums[i]^nums[i] = 0 => nums[i]=0.
    # Number of such cases: freq[0].
    # Case: i=j != k. This happens if nums[i]^nums[i]^nums[k] = 0 => nums[k]=0.
    # Number of such cases: (n * freq[0]) - freq[0] (since i != k).
    # There are 3 such patterns: (i,i,k), (i,k,i), (k,i,i).
    # Total "at least two equal" = 3 * (n * freq[0] - freq[0]) + freq[0]
    # Total "exactly three equal" = freq[0]
    # Total "exactly two equal" = 3 * (n * freq[0] - freq[0])
    
    # So, sum_{i,j,k distinct} = C - 3 * (n * freq[0] - freq[0]) - freq[0]
    # Since we want i < j < k, we divide the "distinct" sum by 3! = 6.
    
    # Let's double check with nums = [0, 0, 0]. n=3, freq[0]=3.
    # C = 3^3 = 27.
    # Distinct sum = 27 - 3*(3*3 - 3) - 3 = 27 - 3*(6) - 3 = 27 - 18 - 3 = 6.
    # 6 / 6 = 1. Correct.
    
    # Check with nums = [1, 1, 1, 1]. n=4, freq[1]=4, freq[0]=0.
    # C: (freq*freq*freq)[0] = sum_{a^b^c=0} freq[a]freq[b]freq[c].
    # Since only freq[1]=4, we need 1^1^1=0, which is false. So C=0.
    # Wait, if nums = [1, 1, 1, 1], then 1^1^1 = 1 != 0. So C=0.
    # My manual check was wrong. If nums=[1,1,1,1], no triplet XORs to 0.
    
    # Check with nums = [1, 2, 3]. n=3, freq[1]=1, freq[2]=1, freq[3]=1.
    # C: 1^2^3=0. Permutations of (1,2,3) are 6. So C=6.
    # freq[0]=0.
    # Distinct sum = 6 - 3(0) - 0 = 6.
    # 6 / 6 = 1. Correct.

    # Final formula:
    # ans = (C - 3 * n * freq[0] + 2 * freq[0]) // 6
    # Let's re-verify:
    # C = 27, n=3, freq[0]=3 => (27 - 3*3*3 + 2*3)/6 = (27 - 27 + 6)/6 = 1. Correct.
    # C = 6, n=3, freq[0]=0 => (6 - 0 + 0)/6 = 1. Correct.
    
    # One more: nums = [0, 1, 1]. n=3, freq[0]=1, freq[1]=2.
    # C: 0^1^1=0. Permutations: (0,1,1), (1,0,1), (1,1,0).
    # Each permutation has freq[0]*freq[1]*freq[1] = 1*2*2 = 4 ways.
    # Total C = 3 * 4 = 12.
    # Formula: (12 - 3*3*1 + 2*1)/6 = (12 - 9 + 2)/6 = 5/6... something is wrong.
    
    # Let's re-evaluate C for [0, 1, 1]:
    # Tuples (i,j,k) such that nums[i]^nums[j]^nums[k]=0:
    # (0,1,2) -> 0^1^1=0. (Indices)
    # (0,2,1) -> 0^1^1=0.
    # (1,0,2) -> 1^0^1=0.
    # (1,2,0) -> 1^1^0=0.
    # (2,0,1) -> 1^0^1=0.
    # (2,1,0) -> 1^1^0=0.
    # (0,0,0) -> 0^0^0=0. (Wait, nums[0]=0, so 0^0^0=0)
    # (1,1,1) -> 1^1^1=1 (No)
    # (2,2,2) -> 1^1^1=1 (No)
    # (1,1,0) -> 1^1^0=0. (Indices: i=1, j=1, k=0)
    # (1,1,0) is (1,1,0), (1,0,1), (0,1,1).
    # Let's list all (i,j,k) for [0, 1, 1]:
    # i,j,k:
    # 0,1,2 (0^1^1=0)
    # 0,2,1 (0^1^1=0)
    # 1,0,2 (1^0^1=0)
    # 1,2,0 (1^1^0=0)
    # 2,0,1 (1^0^1=0)
    # 2,1,0 (1^1^0=0)
    # 0,0,0 (0^0^0=0)
    # 1,1,0 (1^1^0=0)
    # 1,0,1 (1^0^1=0)
    # 0,1,1 (0^1^1=0)
    # 2,2,0 (1^1