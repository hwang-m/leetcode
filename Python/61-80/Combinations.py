class Solution:
    memo = {}
    def combine(self, n: int, k: int) -> List[List[int]]:
        if (n, k) in Solution.memo:
            return Solution.memo[(n, k)]
        if n < k or k == 0:
            return [[]]
        if n == k:
            return [list(range(1, n + 1))]
        
        Solution.memo[(n, k)] = [p + [i] for i in range(k, n + 1) for p in self.combine(i - 1, k - 1)]
        return Solution.memo[(n, k)]
