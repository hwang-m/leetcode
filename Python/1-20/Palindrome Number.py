class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x < 10:
            return True
        if x < 0 or x % 10 == 0:
            return False
        
        q, r = x, 0
        while q != 0:
            q, r = q // 10, r * 10 + q % 10
            if q == r or q // 10 == r:
                return True
        return False
