class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x >= 2**31 or x == 0:
            return 0
        
        if x > 0: q, mult = x, 1
        else: q, mult = -x, -1
            
        ans = 0
        while q > 0:
            q, r = q // 10, q % 10
            ans = ans * 10 + r
        ans = ans * mult
        
        if ans >= 2**31 or ans < -2**31:
            return 0
        return ans
