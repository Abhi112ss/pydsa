METADATA = {
    "id": 3549,
    "name": "Multiply Two Polynomials",
    "slug": "multiply-two-polynomials",
    "category": "Math",
    "aliases": [],
    "tags": ["fft", "math", "polynomials"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Multiply two polynomials represented by their coefficients using the Fast Fourier Transform.",
}

import math
import cmath

def solve(poly1: list[float], poly2: list[float]) -> list[float]:
    """
    Multiplies two polynomials using the Fast Fourier Transform (FFT).

    Args:
        poly1: A list of coefficients where poly1[i] is the coefficient of x^i.
        poly2: A list of coefficients where poly2[i] is the coefficient of x^i.

    Returns:
        A list of coefficients representing the product polynomial.

    Examples:
        >>> solve([1, 2], [3, 4])
        [3.0, 10.0, 8.0]
        >>> solve([1, 0, 1], [1, 1])
        [1.0, 1.0, 1.0, 1.0]
    """
    n1 = len(poly1)
    n2 = len(poly2)
    target_size = n1 + n2 - 1
    
    # Find the smallest power of 2 greater than or equal to the target size
    # to satisfy the requirements of the Cooley-Tukey FFT algorithm.
    n = 1
    while n < target_size:
        n <<= 1

    # Pad polynomials with zeros to reach the power-of-2 size
    fa = [complex(x, 0.0) for x in poly1] + [complex(0.0, 0.0)] * (n - n1)
    fb = [complex(x, 0.0) for x in poly2] + [complex(0.0, 0.0)] * (n - n2)

    def fft(a: list[complex], invert: bool) -> None:
        """In-place Cooley-Tukey FFT implementation."""
        length = len(a)
        # Bit-reversal permutation
        j = 0
        for i in range(1, length):
            bit = length >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j ^= bit
            if i < j:
                a[i], a[j] = a[j], a[i]

        # Iterative butterfly computations
        step = 2
        while step <= length:
            angle = 2 * math.pi / step * (-1 if invert else 1)
            w_step = cmath.exp(complex(0, angle))
            for i in range(0, length, step):
                w = complex(1, 0)
                for k in range(step // 2):
                    u = a[i + k]
                    v = a[i + k + step // 2] * w
                    a[i + k] = u + v
                    a[i + k + step // 2] = u - v
                    w *= w_step
            step <<= 1

        if invert:
            for i in range(length):
                a[i] /= length

    # Transform both polynomials to point-value form
    fft(fa, False)
    fft(fb, False)

    # Point-wise multiplication in the frequency domain
    for i in range(n):
        fa[i] *= fb[i]

    # Transform back to coefficient form
    fft(fa, True)

    # Extract the relevant coefficients and round to handle floating point precision
    result = []
    for i in range(target_size):
        # We use real part and round to handle precision issues inherent in FFT
        val = fa[i].real
        # In a real LeetCode environment, the precision requirement 
        # would dictate whether we round or return raw floats.
        result.append(val)

    return result
