class Solution:
    memo = {0:0}
    def numSquares(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        squares = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        self.memo[n] = 1+ min(self.numSquares(n - square) for square in squares)
        return self.memo[n]
