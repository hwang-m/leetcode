class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == []:
            return [1]
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        return self.plusOne(digits[:-1]) + [0]
