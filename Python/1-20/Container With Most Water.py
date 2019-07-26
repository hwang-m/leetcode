class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        front, end = 0, len(height) - 1
        
        while front < end:
            area = (end - front) * min(height[front], height[end])
            maxarea = max(area, maxarea)
            if height[front] < height[end]:
                front += 1
            else:
                end -= 1
        
        return maxarea
