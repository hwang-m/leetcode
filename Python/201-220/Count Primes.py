class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        # initialize a prime number indicator
        indicator = [1] * n
        # 0 and 1 are not prime
        indicator[0] = 0
        indicator[1] = 0
        
        # go through all the numbers starting from 2
        for i in range(2, n):
            # for every prime number, its multiples are not prime
            if indicator[i] != 0:
                # start from i^2 because those less than i^2 have smaller prime factors
                for x in range(i**2, n, i):
                    indicator[x] = 0
        
        return sum(indicator)
    
