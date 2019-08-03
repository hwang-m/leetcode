class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:   # <- supposed to be 'if x and not n:', but the expected result for 0^0 is 1.0
            return 1.0
        
        if not x:
            return 0.0
        
        if n < 0:
            return self.myPow(1/x, -n)
        
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)
