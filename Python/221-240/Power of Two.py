class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return sum(int(x) for x in bin(n)[2:]) == 1
