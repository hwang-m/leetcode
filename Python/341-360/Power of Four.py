class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and num & int('101010101010101010101010101010101', 2) == num
