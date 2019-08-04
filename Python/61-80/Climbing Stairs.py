class Solution:
    def climbStairs(self, n: int) -> int:
        #Fibonacci numbers
        memo = [1, 2]
        for _ in range(1, n):
            memo = [memo[-1], sum(memo)]
        return memo[-2]
