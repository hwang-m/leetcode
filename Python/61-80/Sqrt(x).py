class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        if left == right:
            return 0
        if right - left == 1:
            return 1
        
        while right - left > 1:
            avg = int((left + right)/2)
            if avg ** 2 == x:
                return avg
            elif avg ** 2 < x:
                left = avg
            else:
                right = avg
        return left
