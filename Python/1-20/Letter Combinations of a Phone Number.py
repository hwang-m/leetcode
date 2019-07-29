class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtoletter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            return []
        
        ans = [[x] for x in list(numtoletter[digits[0]])]
        for num in digits[1:]:
            ans = [x+[y] for x in ans for y in numtoletter[num]]
        
        return [''.join(x) for x in ans]
