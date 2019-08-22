class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        
        while n > 1:
            n2, n3, n5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            ugly.append(min(n2, n3, n5))
            n -= 1
            if n2 == ugly[-1]:
                i2 += 1
            if n3 == ugly[-1]:
                i3 += 1
            if n5 == ugly[-1]:
                i5 += 1
        
        return ugly[-1]
