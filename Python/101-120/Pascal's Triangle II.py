class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        fact = {0:1}
        for i in range(1, rowIndex + 1):
            fact[i] = fact[i - 1] * i
        
        return [fact[rowIndex] / (fact[x] * fact[rowIndex - x]) for x in range(rowIndex + 1)]
