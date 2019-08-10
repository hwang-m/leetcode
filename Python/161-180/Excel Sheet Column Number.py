class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for i, char in enumerate(s[::-1]):
            n += (ord(char) - ord('A') + 1) * (26**i)
        return n
