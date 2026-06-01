METADATA = {
    "id": 1842,
    "name": "Next Palindrome Using Same Digits",
    "slug": "next-palindrome-using-same-digits",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest palindrome that can be formed using the same digits as the given string, which is strictly greater than the input.",
}

def solve(s: str) -> str:
    """
    Args:
        s: The input string representing a number.

    Returns:
        The smallest palindrome greater than s using the same digits, or an empty string if none exists.
    """
    n = len(s)
    digit_counts = {}
    for char in s:
        digit_counts[char] = digit_counts.get(char, 0) + 1

    odd_count = 0
    middle_digit = ""
    for digit, count in digit_counts.items():
        if count % 2 != 0:
            odd_count += 1
            middle_digit = digit

    if odd_count > 1:
        return ""

    half_len = n // 2
    half_digits = []
    for digit in sorted(digit_counts.keys()):
        count = digit_counts[digit]
        if count % 2 != 0:
            count -= 1
        half_digits.extend([digit] * (count // 2))

    def get_palindrome(half_list: list[str], mid: str) -> str:
        left_half = "".join(half_list)
        right_half = left_half[::-1]
        return left_half + mid + right_half

    current_half = list(s[:half_len])
    
    target_half_digits = sorted(half_digits)
    
    def next_permutation(arr: list[str]) -> bool:
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = sorted(arr[i + 1:])
        return True

    def is_valid_half(half_arr: list[str]) -> bool:
        temp_counts = {}
        for char in half_arr:
            temp_counts[char] = temp_counts.get(char, 0) + 1
        for char, count in temp_counts.items():
            if count > digit_counts[char] // 2:
                return False
        return True

    if n % 2 == 0:
        current_half_str = "".join(current_half)
        if current_half_str == "".join(target_half_digits):
            return ""
        
        if next_permutation(current_half):
            if is_valid_half(current_half):
                return get_palindrome(current_half, "")
        
        sorted_half = sorted(half_digits)
        if next_permutation(sorted_half):
            return get_palindrome(sorted_half, "")
        return ""
    else:
        current_half_str = "".join(current_half)
        mid_char = s[half_len]
        
        if current_half_str > "".join(target_half_digits):
            return get_palindrome(target_half_digits, middle_digit)
        
        if current_half_str == "".join(target_half_digits):
            if mid_char < middle_digit:
                return get_palindrome(target_half_digits, middle_digit)
            elif mid_char == middle_digit:
                if next_permutation(half_digits):
                    return get_palindrome(half_digits, middle_digit)
                else:
                    if next_permutation(target_half_digits):
                        return get_palindrome(target_half_digits, middle_digit)
                    return ""
            else:
                return ""
        else:
            if next_permutation(current_half):
                if is_valid_half(current_half):
                    return get_palindrome(current_half, middle_digit)
            
            sorted_half = sorted(half_digits)
            if next_permutation(sorted_half):
                return get_palindrome(sorted_half, middle_digit)
            return ""

def solve(s: str) -> str:
    n = len(s)
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    odds = [char for char, count in counts.items() if count % 2 != 0]
    if len(odds) > 1:
        return ""
    
    mid = odds[0] if odds else ""
    half_elements = []
    for char in sorted(counts.keys()):
        half_elements.extend([char] * (counts[char] // 2))
    
    half_len = n // 2
    target_half = list(s[:half_len])
    
    def get_pal(h_list, m):
        h_str = "".join(h_list)
        return h_str + m + h_str[::-1]

    def is_possible(h_list):
        c = {}
        for x in h_list:
            c[x] = c.get(x, 0) + 1
        for x in c:
            if c[x] > counts[x] // 2:
                return False
        return True

    def next_p(arr):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        if i < 0: return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = sorted(arr[i+1:])
        return True

    if n % 2 == 0:
        if next_p(target_half):
            if is_possible(target_half):
                return get_pal(target_half, "")
        
        sorted_half = sorted(half_elements)
        if next_p(sorted_half):
            return get_pal(sorted_half, "")
        return ""
    else:
        current_mid = s[half_len]
        sorted_half = sorted(half_elements)
        
        if target_half > sorted_half:
            return get_pal(sorted_half, mid)
        
        if target_half == sorted_half:
            if current_mid < mid:
                return get_pal(sorted_half, mid)
            elif current_mid == mid:
                if next_p(target_half):
                    if is_possible(target_half):
                        return get_pal(target_half, mid)
                if next_p(sorted_half):
                    return get_pal(sorted_half, mid)
                return ""
            else:
                return ""
        else:
            if next_p(target_half):
                if is_possible(target_half):
                    return get_pal(target_half, mid)
            if next_p(sorted_half):
                return get_pal(sorted_half, mid)
            return ""