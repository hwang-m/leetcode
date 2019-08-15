class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        
        steps = {n}
        while n != 1:
            sum_of_squares = 0
            for char in str(n):
                sum_of_squares += int(char) ** 2
            n = sum_of_squares
            if n in steps:
                break
            else:
                steps.add(n)
        return n == 1
