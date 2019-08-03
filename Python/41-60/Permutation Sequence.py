class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remaining = [str(i) for i in range(1, n + 1)]
        ans = []
        
        while remaining and k > 0:
            n = len(remaining)
            q, k = remaining.pop((k - 1) // math.factorial(n - 1)), (k - 1) % math.factorial(n - 1) + 1
            ans.append(q)
        
        return ''.join(ans + remaining)
