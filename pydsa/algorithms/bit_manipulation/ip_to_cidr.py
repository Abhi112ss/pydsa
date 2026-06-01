METADATA = {
    "id": 751,
    "name": "IP to CIDR",
    "slug": "ip_to_cidr",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a range of IP addresses into the minimum number of CIDR blocks.",
}

def solve(ip_range: list[str], ip_count: int) -> list[str]:
    """
    Converts a starting IP address and a count of consecutive IPs into the 
    minimum number of CIDR blocks.

    Args:
        ip_range: A list containing a single string representing the starting IP address.
        ip_count: The number of consecutive IP addresses to cover.

    Returns:
        A list of strings, where each string is a CIDR block in 'IP/prefix' format.

    Examples:
        >>> solve(["255.0.0.7"], 10)
        ['255.0.0.7/32', '255.0.0.8/29', '255.0.0.16/32']
    """

    def ip_to_int(ip: str) -> int:
        """Converts a dotted-decimal IP string to a 32-bit integer."""
        parts = list(map(int, ip.split('.')))
        return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

    def int_to_ip(n: int) -> str:
        """Converts a 32-bit integer to a dotted-decimal IP string."""
        return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"

    current_ip_int = ip_to_int(ip_range[0])
    remaining_count = ip_count
    result = []

    while remaining_count > 0:
        # Step 1: Find the largest power of 2 that divides the current IP integer.
        # This is the 'lowbit' trick: (x & -x) gives the value of the lowest set bit.
        # This bit determines the maximum possible size of a CIDR block starting here.
        lowbit = current_ip_int & -current_ip_int
        
        # If current_ip_int is 0, lowbit will be 0. We handle this by treating it 
        # as a very large power of 2 (though in 32-bit IP context, 2^32 is the limit).
        if lowbit == 0:
            # For IP 0.0.0.0, the lowbit logic needs a fallback. 
            # However, in bit manipulation, 0 is a special case.
            # We can find the largest power of 2 that is <= remaining_count.
            # But actually, for 0.0.0.0, we can use the largest power of 2 
            # that doesn't exceed the remaining count and fits the alignment.
            # A simpler way: find the largest power of 2 <= remaining_count.
            # But CIDR blocks must be aligned to their size. 
            # For 0.0.0.0, any power of 2 is aligned.
            max_size = 1 << (remaining_count.bit_length() - 1)
        else:
            # The size of the block is limited by the alignment (lowbit) 
            # and the number of IPs we actually have left.
            # We find the largest power of 2 that is <= lowbit AND <= remaining_count.
            # Since lowbit is already a power of 2, we just check remaining_count.
            max_size = 1 << (lowbit.bit_length() - 1)
            
            # If the lowbit is larger than the remaining count, we must cap it.
            # We find the largest power of 2 <= remaining_count.
            if max_size > remaining_count:
                max_size = 1 << (remaining_count.bit_length() - 1)

        # Step 2: Calculate the prefix length.
        # A block of size 2^k has a prefix length of 32 - k.
        # We use the bit_length of max_size to find k.
        k = max_size.bit_length() - 1
        prefix = 32 - k
        
        # Step 3: Add the CIDR block to the result and update state.
        result.append(f"{int_to_ip(current_ip_int)}/{prefix}")
        
        current_ip_int += max_size
        remaining_count -= max_size

    return result
