class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        end = len(numbers) - 1
        
        while end > front:
            while numbers[front] + numbers[end] > target:
                end -= 1
            if numbers[front] + numbers[end] == target:
                return [front + 1, end + 1]
            else:
                front += 1
