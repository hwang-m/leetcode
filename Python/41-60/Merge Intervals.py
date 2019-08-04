class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        ans = [intervals[0]]
        
        def merge_two(A: List[int], B: List[int]) -> List[int]:
            return [min(A[0], B[0]), max(A[1], B[1])]
        
        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]:
                ans[-1] = merge_two(ans[-1], interval)
            else:
                ans.append(interval)
                
        return ans
