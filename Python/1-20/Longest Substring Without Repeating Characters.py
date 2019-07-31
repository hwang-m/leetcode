class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = maxlength = 0
        
        for i, char in enumerate(s):
            if not char in seen:
                length += 1
                seen[char] = i
            else:
                maxlength = max(maxlength, length)
                length = min(length + 1, i - seen[char])
                seen[char] = i
        
        return max(length, maxlength)
