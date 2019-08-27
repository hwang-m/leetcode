class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3: return 1
        if n == 3: return 2
        # if n > 3
        q, r = n // 3, n % 3
        if r == 0:
            return 3**q
        if r == 1:
            return 3**(q-1) * 4
        if r == 2:
            return 3**q * 2
