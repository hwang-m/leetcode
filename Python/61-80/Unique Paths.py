class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Assume that m and n are positive integers.
        # The robot makes (m+n-2) moves in total no matter what path it takes.
        # Choose (n-1) places to move down from the total (m+n-1) moves.
        
        # The following line gives 56 (int(56.9999999)) for test case (57, 2).
        # return int(math.factorial(m+n-2) / math.factorial(n-1) / math.factorial(m-1))
        
        # this works:
        return math.factorial(m+n-2) // math.factorial(n-1) // math.factorial(m-1)
        
        # this also works:
        # s, l = min(m-1, n-1), max(m-1, n-1)
        # ans = 1
        #
        # for i in range(s):
        #     ans *= l+i+1
        #    
        # return int(ans/math.factorial(s))
