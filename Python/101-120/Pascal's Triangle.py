class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        fact = {0:1}
        for i in range(1, numRows):
            fact[i] = fact[i - 1] * i
        
        ans = []
        for row in range(numRows):
            ans.append([fact[row] / (fact[x] * fact[row - x]) for x in range(row + 1)])
        
        return ans
