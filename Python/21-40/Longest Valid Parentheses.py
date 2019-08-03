class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        def longest_from_the_left(s, left):
            maxlen = 0
            current_len = 0
            open_paren = 0
            for char in s:
                current_len += 1
                if char == left:
                    open_paren += 1
                else:
                    open_paren -= 1
                    if open_paren < 0:
                        current_len = 0
                        open_paren = 0
                    elif open_paren == 0:
                        maxlen = max(maxlen, current_len)
            return maxlen
    
        return max(longest_from_the_left(s, '('), longest_from_the_left(s[::-1], ')'))
