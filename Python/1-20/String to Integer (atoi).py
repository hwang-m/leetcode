class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        ans = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i == len(str):
            return 0
        
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign *= -1
            i += 1
        
        while i < len(str) and str[i].isdigit():
            ans = ans * 10 + int(str[i])
            i += 1
        
        if sign == 1:
            return min(ans, 2**31 - 1)
        else:
            return max(sign * ans, -2**31)
