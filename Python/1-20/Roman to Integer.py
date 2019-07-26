class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        store = 0
        ans = 0
        
        for char in s[::-1]:
            if roman[char] < store:
                ans -= roman[char]
            else:
                ans += roman[char]
            store = roman[char]
            
        return ans
