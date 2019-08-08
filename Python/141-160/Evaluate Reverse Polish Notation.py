class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        nums = []
        
        for i, char in enumerate(tokens):
            if not char in operators:
                nums.append(char)
            else:
                m, n = int(nums.pop()), int(nums.pop())
                if char == '+':
                    nums.append(n + m)
                elif char == '-':
                    nums.append(n - m)
                elif char == '*':
                    nums.append(n * m)
                else:
                    nums.append(int(n / m))
        
        return nums.pop()
