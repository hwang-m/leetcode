class Solution:
    
    memo = {0:[0], 1:[0,1]}
    
    def grayCode(self, n: int) -> List[int]:
        if n in Solution.memo:
            return Solution.memo[n]
        
        prev = self.grayCode(n-1)
        second_half = ['1'+bin(i)[2:].zfill(n-1) for i in prev[::-1]]
        
        Solution.memo[n] = prev + [int(s, 2) for s in second_half]
        return Solution.memo[n]
