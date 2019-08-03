class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split()
        if not ls:
            return 0
        return len(ls[-1])
