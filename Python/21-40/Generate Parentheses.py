class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        
        ans = []
        for c in range(n):
            ans.extend(['({}){}'.format(left, right) for left in self.generateParenthesis(c) for right in self.generateParenthesis(n - c - 1)])
        return ans
