class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                ls.append(char)
            elif char == ')':
                if len(ls) == 0 or ls[-1] != '(':
                    return False
                else:
                    ls.pop()
            elif char == ']':
                if len(ls) == 0 or ls[-1] != '[':
                    return False
                else:
                    ls.pop()
            else:
                if len(ls) == 0 or ls[-1] != '{':
                    return False
                else:
                    ls.pop()
        return len(ls) == 0
